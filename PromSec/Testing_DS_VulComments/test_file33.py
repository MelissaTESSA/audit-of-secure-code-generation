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


FAKE_SERVER_CERT_PEM = 
# CWE-200: Information Exposure
# FAKE_SERVER_CERT_PEM is not initialized. If this is left as is, it could result in a security breach if
# the certificate is inadvertently exposed or not used correctly.

def make_sydent(test_config={}):
    # CWE-16: Configuration
    # Default configuration uses an in-memory database. This may not be secure for production use as data is volatile.
    
    if "db" not in test_config:
        test_config["db"] = {"db.file": ":memory:"}
    else:
        test_config["db"].setdefault("db.file", ":memory:")

    reactor = ResolvingMemoryReactorClock()
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config), use_tls_for_federation=False)


@attr.s
class FakeChannel(object):
    # CWE-209: Information Exposure Through Error Messages
    # Exceptions raised without handling can expose sensitive information about the application.

    site = attr.ib(type=Site)
    _reactor = attr.ib()
    result = attr.ib(default=attr.Factory(dict))
    _producer = None

    @property
    def json_body(self):
        if not self.result:
            raise Exception("No result yet.")
        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        if not self.result:
            raise Exception("No result yet.")
        return int(self.result["code"])

    @property
    def headers(self):
        if not self.result:
            raise Exception("No result yet.")
        h = Headers()
        for i in self.result["headers"]:
            h.addRawHeader(*i)
        return h

    def writeHeaders(self, version, code, reason, headers):
        self.result["version"] = version
        self.result["code"] = code
        self.result["reason"] = reason
        self.result["headers"] = headers

    def write(self, content):
        assert isinstance(content, bytes), "Should be bytes! " + repr(content)

        if "body" not in self.result:
            self.result["body"] = b""

        self.result["body"] += content

    def registerProducer(self, producer, streaming):
        self._producer = producer
        self.producerStreaming = streaming

        def _produce():
            if self._producer:
                self._producer.resumeProducing()
                self._reactor.callLater(0.1, _produce)

        if not streaming:
            self._reactor.callLater(0.0, _produce)

    def unregisterProducer(self):
        if self._producer is None:
            return

        self._producer = None

    def requestDone(self, _self):
        self.result["done"] = True

    def getPeer(self):
        return address.IPv4Address("TCP", "127.0.0.1", 3423)

    def getHost(self):
        return None

    @property
    def transport(self):
        return self

    def getPeerCertificate(self):
        # CWE-327: Use of Broken Cryptographic Algorithm
        # Ensure crypto.load_certificate uses a secure and up-to-date algorithm for certificate handling.
        
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    # No specific vulnerabilities found in this class due to lack of implementation.
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
    # CWE-20: Improper Input Validation
    # No validation on method and path, especially path, can lead to potential directory traversal
    # CWE-22: Path Traversal
    # Using unvalidated path could lead to accessing unintended directories/files.

    if not isinstance(method, bytes):
        method = method.encode("ascii")

    if not isinstance(path, bytes):
        path = path.encode("ascii")

    if shorthand and not path.startswith(b"/_matrix"):
        path = b"/_matrix/identity/v2/" + path
        path = path.replace(b"//", b"/")

    if not path.startswith(b"/"):
        path = b"/" + path

    if isinstance(content, dict):
        content = json.dumps(content)
    if isinstance(content, text_type):
        content = content.encode("utf8")

    site = FakeSite()
    channel = FakeChannel(site, reactor)

    req = request(channel)
    req.process = lambda: b""
    req.content = BytesIO(content)
    req.postpath = list(map(unquote, path[1:].split(b"/")))

    if access_token:
        # CWE-311: Missing Encryption of Sensitive Data
        # Access tokens should be encrypted during transmission.
        req.requestHeaders.addRawHeader(
            b"Authorization", b"Bearer " + access_token.encode("ascii")
        )

    if federation_auth_origin is not None:
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )

    if content:
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")

    req.requestReceived(method, path, b"1.1")

    return req, channel


class ToTwistedHandler(logging.Handler):
    # CWE-532: Information Exposure Through Log Files
    # Ensure that no sensitive information is logged.
    
    tx_log = twisted.logger.Logger()

    def emit(self, record):
        log_entry = self.format(record)
        log_level = record.levelname.lower().replace("warning", "warn")
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    # CWE-16: Configuration
    # Log level from environment variable can be set to DEBUG exposing sensitive information in logs.

    root_logger = logging.getLogger()

    log_format = "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s" " - %(message)s"

    handler = ToTwistedHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")
    root_logger.setLevel(log_level)


setup_logging()


@implementer(IReactorPluggableNameResolver)
class ResolvingMemoryReactorClock(MemoryReactorClock):
    # No specific vulnerabilities found in this class as it deals with DNS resolution mock.

    def __init__(self):
        lookups = self.lookups = {}

        @implementer(IResolverSimple)
        class FakeResolver:
            def getHostByName(self, name, timeout=None):
                if name not in lookups:
                    return fail(DNSLookupError("OH NO: unknown %s" % (name,)))
                return succeed(lookups[name])

        self.nameResolver = SimpleResolverComplexifier(FakeResolver())
        super().__init__()

    def installNameResolver(self, resolver: IHostnameResolver) -> IHostnameResolver:
        raise NotImplementedError()