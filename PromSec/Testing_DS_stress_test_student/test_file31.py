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
    # Let's create a Sydent object with some default config
    if "db" not in test_config:
        test_config["db"] = {"db.file": ":memory:"}  # Use an in-memory database if not specified
    else:
        test_config["db"].setdefault("db.file", ":memory:")  # Ensure db.file is set

    reactor = ResolvingMemoryReactorClock()  # Make a fake reactor clock
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config), use_tls_for_federation=False)


@attr.s
class FakeChannel(object):
    # This class simulates a network channel for requests

    site = attr.ib(type=Site)  # The site this channel is part of
    _reactor = attr.ib()  # The reactor, which is like the event loop
    result = attr.ib(default=attr.Factory(dict))  # Store the result of the request here
    _producer = None  # Placeholder for a producer, which makes content

    @property
    def json_body(self):
        # Convert the body of the result to JSON
        if not self.result:
            raise Exception("No result yet.")  # If there's no result yet, raise an error
        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        # Get the HTTP response code
        if not self.result:
            raise Exception("No result yet.")
        return int(self.result["code"])

    @property
    def headers(self):
        # Get the response headers
        if not self.result:
            raise Exception("No result yet.")
        h = Headers()
        for i in self.result["headers"]:
            h.addRawHeader(*i)  # Add headers one by one
        return h

    def writeHeaders(self, version, code, reason, headers):
        # Write headers to the result
        self.result["version"] = version
        self.result["code"] = code
        self.result["reason"] = reason
        self.result["headers"] = headers

    def write(self, content):
        # Write content to the body
        assert isinstance(content, bytes), "Should be bytes! " + repr(content)

        if "body" not in self.result:
            self.result["body"] = b""

        self.result["body"] += content  # Add the content to the body

    def registerProducer(self, producer, streaming):
        # Register a producer to generate content
        self._producer = producer
        self.producerStreaming = streaming

        def _produce():
            if self._producer:
                self._producer.resumeProducing()
                self._reactor.callLater(0.1, _produce)  # Keep producing every 0.1 seconds

        if not streaming:
            self._reactor.callLater(0.0, _produce)

    def unregisterProducer(self):
        # Stop the producer
        if self._producer is None:
            return

        self._producer = None

    def requestDone(self, _self):
        # Mark the request as done
        self.result["done"] = True

    def getPeer(self):
        # Get the peer address (fake one)
        return address.IPv4Address("TCP", "127.0.0.1", 3423)

    def getHost(self):
        # Get the host address (can be None)
        return None

    @property
    def transport(self):
        # Transport is itself for this fake channel
        return self

    def getPeerCertificate(self):
        # Return a fake certificate for the server
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    # Just a placeholder class for a site
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
    Make a web request using the given method and path, feed it the
    content, and return the Request and the Channel underneath. Mostly
    to test how requests are handled.

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
    if not isinstance(method, bytes):
        method = method.encode("ascii")  # Ensure method is in bytes

    if not isinstance(path, bytes):
        path = path.encode("ascii")  # Ensure path is in bytes

    if shorthand and not path.startswith(b"/_matrix"):
        path = b"/_matrix/identity/v2/" + path  # Add default prefix if missing
        path = path.replace(b"//", b"/")

    if not path.startswith(b"/"):
        path = b"/" + path  # Ensure path starts with a slash

    if isinstance(content, dict):
        content = json.dumps(content)  # Convert dict content to JSON
    if isinstance(content, text_type):
        content = content.encode("utf8")  # Ensure content is in bytes

    site = FakeSite()  # Create a fake site
    channel = FakeChannel(site, reactor)  # Create a channel using the fake site

    req = request(channel)  # Create a request object
    req.process = lambda: b""  # Empty process function
    req.content = BytesIO(content)  # Use BytesIO for request content
    req.postpath = list(map(unquote, path[1:].split(b"/")))  # Set the path

    if access_token:
        req.requestHeaders.addRawHeader(
            b"Authorization", b"Bearer " + access_token.encode("ascii")
        )  # Add access token to headers if provided

    if federation_auth_origin is not None:
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )  # Add fake federation auth header

    if content:
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")  # Set content type

    req.requestReceived(method, path, b"1.1")  # Simulate receiving the request

    return req, channel  # Return the request and channel


class ToTwistedHandler(logging.Handler):
    # Custom logging handler to integrate with Twisted's logging
    tx_log = twisted.logger.Logger()  # Twisted logger instance

    def emit(self, record):
        log_entry = self.format(record)  # Format the log record
        log_level = record.levelname.lower().replace("warning", "warn")  # Get the log level
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )  # Emit the log entry


def setup_logging():
    # Set up logging for the application
    root_logger = logging.getLogger()  # Get the root logger

    log_format = "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s" " - %(message)s"  # Log format

    handler = ToTwistedHandler()  # Create our custom handler
    formatter = logging.Formatter(log_format)  # Create a formatter
    handler.setFormatter(formatter)  # Set the formatter on handler
    root_logger.addHandler(handler)  # Add handler to the root logger

    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")  # Get log level from environment
    root_logger.setLevel(log_level)  # Set the log level


setup_logging()  # Call the setup_logging function to initialize logging


@implementer(IReactorPluggableNameResolver)
class ResolvingMemoryReactorClock(MemoryReactorClock):
    # A custom reactor clock that can resolve hostnames

    def __init__(self):
        lookups = self.lookups = {}  # Dictionary to store hostname lookups

        @implementer(IResolverSimple)
        class FakeResolver:
            def getHostByName(self, name, timeout=None):
                if name not in lookups:
                    return fail(DNSLookupError("OH NO: unknown %s" % (name,)))
                return succeed(lookups[name])  # Return the resolved address

        self.nameResolver = SimpleResolverComplexifier(FakeResolver())  # Use our fake resolver
        super().__init__()  # Call the parent constructor

    def installNameResolver(self, resolver: IHostnameResolver) -> IHostnameResolver:
        raise NotImplementedError()  # Not implemented yet!