import json
from io import BytesIO
import logging
import os
from typing import Dict
import attr
from six import text_type
from zope.interface import implementer
from twisted.internet._resolver import SimpleResolverComplexifier
from twisted.internet.defer import fail, succeed
from twisted.internet.error import DNSLookupError
from twisted.internet.interfaces import (
    IHostnameResolver,
    IReactorPluggableNameResolver,
    IResolverSimple,
)

from twisted.internet import address
import twisted.logger
from twisted.web.http_headers import Headers
from twisted.web.server import Request, Site
from twisted.web.http import unquote
from twisted.test.proto_helpers import MemoryReactorClock
from OpenSSL import crypto

from sydent.sydent import Sydent, parse_config_dict


FAKE_SERVER_CERT_PEM = """
-----BEGIN CERTIFICATE-----
MIIDlzCCAn+gAwIBAgIUC8tnJVZ8Cawh5tqr7PCAOfvyGTYwDQYJKoZIhvcNAQEL
BQAwWzELMAkGA1UEBhMCQVUxEzARBgNVBAgMClNvbWUtU3RhdGUxITAfBgNVBAoM
GEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZDEUMBIGA1UEAwwLZmFrZS5zZXJ2ZXIw
HhcNMjAwMTE0MTc1MzQwWhcNMzAwMTExMTc1MzQwWjBbMQswCQYDVQQGEwJBVTET
MBEGA1UECAwKU29tZS1TdGF0ZTEhMB8GA1UECgwYSW50ZXJuZXQgV2lkZ2l0cyBQ
dHkgTHRkMRQwEgYDVQQDDAtmYWtlLnNlcnZlcjCCASIwDQYJKoZIhvcNAQEBBQAD
ggEPADCCAQoCggEBANNzY7YHBLm4uj52ojQc/dfQCoR+63IgjxZ6QdnThhIlOYgE
3y0Ks49bt3GKmAweOFRRKfDhJRKCYfqZTYudMcdsQg696s2HhiTY0SpqO0soXwW4
6kEIxnTy2TqkPjWlsWgGTtbVnKc5pnLs7MaQwLIQfxirqD2znn+9r68WMOJRlzkv
VmrXDXjxKPANJJ9b0PiGrL2SF4QcF3zHk8Tjf24OGRX4JTNwiGraU/VN9rrqSHug
CLWcfZ1mvcav3scvtGfgm4kxcw8K6heiQAc3QAMWIrdWhiunaWpQYgw7euS8lZ/O
C7HZ7YbdoldknWdK8o7HJZmxUP9yW9Pqa3n8p9UCAwEAAaNTMFEwHQYDVR0OBBYE
FHwfTq0Mdk9YKqjyfdYm4v9zRP8nMB8GA1UdIwQYMBaAFHwfTq0Mdk9YKqjyfdYm
4v9zRP8nMA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAEPVM5/+
Sj9P/CvNG7F2PxlDQC1/+aVl6ARAz/bZmm7yJnWEleBSwwFLerEQU6KFrgjA243L
qgY6Qf2EYUn1O9jroDg/IumlcQU1H4DXZ03YLKS2bXFGj630Piao547/l4/PaKOP
wSvwDcJlBatKfwjMVl3Al/EcAgUJL8eVosnqHDSINdBuFEc8Kw4LnDSFoTEIx19i
c+DKmtnJNI68wNydLJ3lhSaj4pmsX4PsRqsRzw+jgkPXIG1oGlUDMO3k7UwxfYKR
XkU5mFYkohPTgxv5oYGq2FCOPixkbov7geCEvEUs8m8c8MAm4ErBUzemOAj8KVhE
tWVEpHfT+G7AjA8=
-----END CERTIFICATE-----
"""


def make_sydent(test_config={}):
    # Creating a fake Sydent instance with some default configuration.
    # If the 'db' key isn't in the test config, add it with an in-memory DB file.
    if "db" not in test_config:
        test_config["db"] = {"db.file": ":memory:"}
    else:
        test_config["db"].setdefault("db.file", ":memory:")

    # Making a fake reactor that handles time and DNS stuff.
    reactor = ResolvingMemoryReactorClock()
    # Returning a Sydent instance with the reactor and parsed config.
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config), use_tls_for_federation=False)


@attr.s
class FakeChannel(object):
    # This is like a fake network channel that simulates HTTP requests and responses.

    site = attr.ib(type=Site)
    _reactor = attr.ib()
    result = attr.ib(default=attr.Factory(dict))
    _producer = None

    @property
    def json_body(self):
        # Decodes the body of the result as JSON.
        if not self.result:
            raise Exception("No result yet.")
        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        # Returns the HTTP status code of the result.
        if not self.result:
            raise Exception("No result yet.")
        return int(self.result["code"])

    @property
    def headers(self):
        # Returns the HTTP headers of the result.
        if not self.result:
            raise Exception("No result yet.")
        h = Headers()
        for i in self.result["headers"]:
            h.addRawHeader(*i)
        return h

    def writeHeaders(self, version, code, reason, headers):
        # Saves the HTTP response headers.
        self.result["version"] = version
        self.result["code"] = code
        self.result["reason"] = reason
        self.result["headers"] = headers

    def write(self, content):
        # Writes content to the response body, making sure it's bytes.
        assert isinstance(content, bytes), "Should be bytes! " + repr(content)

        if "body" not in self.result:
            self.result["body"] = b""

        self.result["body"] += content

    def registerProducer(self, producer, streaming):
        # Registers a producer to manage streaming data.
        self._producer = producer
        self.producerStreaming = streaming

        def _produce():
            if self._producer:
                self._producer.resumeProducing()
                self._reactor.callLater(0.1, _produce)

        if not streaming:
            self._reactor.callLater(0.0, _produce)

    def unregisterProducer(self):
        # Unregisters the current producer.
        if self._producer is None:
            return

        self._producer = None

    def requestDone(self, _self):
        # Marks the request as done.
        self.result["done"] = True

    def getPeer(self):
        # Simulates getting the peer's address.
        return address.IPv4Address("TCP", "127.0.0.1", 3423)

    def getHost(self):
        # Doesn't return a host, just None.
        return None

    @property
    def transport(self):
        # Returns self as the transport, kind of like pretending to be the network layer.
        return self

    def getPeerCertificate(self):
        # Loads and returns a fake server certificate.
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    # Just a placeholder for a fake site.
    pass


def make_request(
    reactor,
    method,
    path,
    content=b"",
    access_token=None,
    request=Request,
    shorthand=True,
    federation_auth_origin=None,
):
    """
    This function makes a web request using the specified method and path.
    It feeds the content to the request and returns the Request and the Channel.

    Args:
        reactor (IReactor): The Twisted reactor to use when performing the request.
        method (bytes or unicode): The HTTP request method ("verb").
        path (bytes or unicode): The HTTP path, suitably URL encoded (e.g.
        escaped UTF-8 & spaces and such).
        content (bytes or dict): The body of the request. JSON-encoded, if
        a dict.
        access_token (unicode): An access token to use to authenticate the request,
            None if no access token needs to be included.
        request (IRequest): The class to use when instantiating the request object.
        shorthand: Whether to try and be helpful and prefix the given URL
        with the usual REST API path, if it doesn't contain it.
        federation_auth_origin (bytes|None): if set to not-None, we will add a fake
            Authorization header pretending to be the given server name.

    Returns:
        Tuple[synapse.http.site.SynapseRequest, channel]
    """
    # Convert method to bytes if it's not already.
    if not isinstance(method, bytes):
        method = method.encode("ascii")

    # Convert path to bytes if it's not already.
    if not isinstance(path, bytes):
        path = path.encode("ascii")

    # If shorthand is True and path doesn't start with '/_matrix', add it.
    if shorthand and not path.startswith(b"/_matrix"):
        path = b"/_matrix/identity/v2/" + path
        path = path.replace(b"//", b"/")

    # Ensure path starts with a '/'.
    if not path.startswith(b"/"):
        path = b"/" + path

    # Convert content to JSON bytes if it's a dict.
    if isinstance(content, dict):
        content = json.dumps(content)
    if isinstance(content, text_type):
        content = content.encode("utf8")

    # Create a fake site and channel for the request.
    site = FakeSite()
    channel = FakeChannel(site, reactor)

    # Make a request object and set up its properties.
    req = request(channel)
    req.process = lambda: b""
    req.content = BytesIO(content)
    req.postpath = list(map(unquote, path[1:].split(b"/")))

    # Add authorization header if access_token is provided.
    if access_token:
        req.requestHeaders.addRawHeader(
            b"Authorization", b"Bearer " + access_token.encode("ascii")
        )

    # Add fake federation authorization header if federation_auth_origin is not None.
    if federation_auth_origin is not None:
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )

    # Add content type header if content exists.
    if content:
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")

    # Simulate receiving the request.
    req.requestReceived(method, path, b"1.1")

    return req, channel


class ToTwistedHandler(logging.Handler):
    # A custom logging handler that sends log messages to Twisted logs.

    tx_log = twisted.logger.Logger()

    def emit(self, record):
        # Format and emit a log record to the Twisted logger.
        log_entry = self.format(record)
        log_level = record.levelname.lower().replace("warning", "warn")
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    # Sets up logging for the application.

    root_logger = logging.getLogger()

    # Define the log format.
    log_format = "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s" " - %(message)s"

    # Create a handler that sends log messages to Twisted.
    handler = ToTwistedHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)

    # Add the handler to the root logger.
    root_logger.addHandler(handler)

    # Set the log level from an environment variable, defaulting to ERROR.
    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")
    root_logger.setLevel(log_level)


setup_logging()


@implementer(IReactorPluggableNameResolver)
class ResolvingMemoryReactorClock(MemoryReactorClock):
    # This class extends a memory reactor clock with DNS name resolution.

    def __init__(self):
        # Initialize with an empty dictionary for lookups.
        lookups = self.lookups = {}

        @implementer(IResolverSimple)
        class FakeResolver:
            # A fake resolver that simulates DNS lookups.
            def getHostByName(self, name, timeout=None):
                # Fail if the name isn't in lookups, otherwise succeed with the stored address.
                if name not in lookups:
                    return fail(DNSLookupError("OH NO: unknown %s" % (name,)))
                return succeed(lookups[name])

        # Set the name resolver to a simple resolver that uses the fake resolver.
        self.nameResolver = SimpleResolverComplexifier(FakeResolver())
        super().__init__()

    def installNameResolver(self, resolver: IHostnameResolver) -> IHostnameResolver:
        # This method isn't implemented yet.
        raise NotImplementedError()