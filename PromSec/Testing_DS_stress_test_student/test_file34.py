import json
from io import BytesIO
import logging
import os

import attr
from six import text_type
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
    # This function makes a Sydent instance. If no database is in the test config,
    # it gives it a default in-memory database. That's cool because you don't need a real database for tests!
    if 'db' not in test_config:
        test_config['db'] = {'db.file': ':memory:'}
    else:
        test_config['db'].setdefault('db.file', ':memory:')

    reactor = MemoryReactorClock()  # Create a fake reactor for time-based stuff!
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config))


@attr.s
class FakeChannel(object):
    # This is a fake channel that simulates network communication. It's useful for testing
    # without actually connecting to the network!

    site = attr.ib(type=Site)  # The site this channel is associated with.
    _reactor = attr.ib()  # The reactor for simulating time-based operations.
    result = attr.ib(default=attr.Factory(dict))  # Stores the result of the request.
    _producer = None  # This will be set to the producer of the content.

    @property
    def json_body(self):
        # Returns the JSON body of the response, which is pretty handy!
        if not self.result:
            raise Exception("No result yet.")
        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        # Returns the HTTP response code, like 200 for success!
        if not self.result:
            raise Exception("No result yet.")
        return int(self.result["code"])

    @property
    def headers(self):
        # Returns the HTTP headers of the response.
        if not self.result:
            raise Exception("No result yet.")
        h = Headers()
        for i in self.result["headers"]:
            h.addRawHeader(*i)
        return h

    def writeHeaders(self, version, code, reason, headers):
        # Writes headers to the result. This is what happens when the server responds!
        self.result["version"] = version
        self.result["code"] = code
        self.result["reason"] = reason
        self.result["headers"] = headers

    def write(self, content):
        # Writes content to the body of the response. It's like the server sending data back!
        assert isinstance(content, bytes), "Should be bytes! " + repr(content)

        if "body" not in self.result:
            self.result["body"] = b""

        self.result["body"] += content

    def registerProducer(self, producer, streaming):
        # Registers a producer to produce content. Streaming means it can send data over time!
        self._producer = producer
        self.producerStreaming = streaming

        def _produce():
            if self._producer:
                self._producer.resumeProducing()
                self._reactor.callLater(0.1, _produce)

        if not streaming:
            self._reactor.callLater(0.0, _produce)

    def unregisterProducer(self):
        # Unregisters the producer, meaning we're done sending data!
        if self._producer is None:
            return

        self._producer = None

    def requestDone(self, _self):
        # Marks the request as done, which is like saying "we're finished!"
        self.result["done"] = True

    def getPeer(self):
        # Returns a fake peer address. This is who we're "talking" to!
        return address.IPv4Address("TCP", "127.0.0.1", 3423)

    def getHost(self):
        # Returns the host address. It's None because we don't need it here!
        return None

    @property
    def transport(self):
        # This is a trick to make the transport look like the channel itself!
        return self

    def getPeerCertificate(self):
        # Returns a fake server certificate. It's like pretending we have a secure connection!
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    # This is a fake site class. It's empty because we just need it as a placeholder!
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
    # This function makes a web request with the given method and path.
    # It's super helpful for testing how requests are handled.

    if not isinstance(method, bytes):
        method = method.encode("ascii")  # Make sure method is in bytes!

    if not isinstance(path, bytes):
        path = path.encode("ascii")  # Make sure path is in bytes!

    if (
        shorthand
        and not path.startswith(b"/_matrix")
    ):
        # If shorthand is true, it adds a default path prefix. That's neat!
        path = b"/_matrix/identity/v2/" + path
        path = path.replace(b"//", b"/")

    if not path.startswith(b"/"):
        path = b"/" + path  # Ensure path always starts with "/"

    if isinstance(content, dict):
        content = json.dumps(content)  # Convert dict content to JSON
    if isinstance(content, text_type):
        content = content.encode("utf8")  # Make sure content is in bytes

    site = FakeSite()
    channel = FakeChannel(site, reactor)

    req = request(channel)
    req.process = lambda: b""
    req.content = BytesIO(content)  # Store content in a BytesIO object
    req.postpath = list(map(unquote, path[1:].split(b"/")))  # Split path into components

    if access_token:
        # Add an Authorization header if we have an access token. It's like logging in!
        req.requestHeaders.addRawHeader(
            b"Authorization", b"Bearer " + access_token.encode("ascii")
        )

    if federation_auth_origin is not None:
        # Add a fake Federation Authorization header. This is for simulating server-to-server requests!
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )

    if content:
        # Add a Content-Type header if there's content. This tells the server what kind of content we're sending!
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")

    req.requestReceived(method, path, b"1.1")  # Simulate the request being received

    return req, channel  # Return the request and channel for further processing


class ToTwistedHandler(logging.Handler):
    # This logging handler sends logs to the Twisted logging system. It's like connecting two different logging systems!
    tx_log = twisted.logger.Logger()

    def emit(self, record):
        # This function gets called whenever there's a log record to handle.
        log_entry = self.format(record)  # Format the log record
        log_level = record.levelname.lower().replace("warning", "warn")  # Adjust log level names
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    # This function sets up logging. It's good to have logs to see what's happening in the code!
    root_logger = logging.getLogger()

    log_format = (
        "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s"
        " - %(message)s"
    )  # Define the format for log messages

    handler = ToTwistedHandler()  # Use our custom handler for logging
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)  # Add the handler to the root logger

    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")  # Get log level from environment
    root_logger.setLevel(log_level)  # Set the log level for the root logger


setup_logging()  # Call the function to set up logging when the script runs