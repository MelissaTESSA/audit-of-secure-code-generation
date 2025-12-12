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


FAKE_SERVER_CERT_PEM = 
# CWE-200: Information Exposure
# The certificate is stored in a global variable and its content is not shown here.
# If this variable is exposed elsewhere in the code, it could lead to sensitive information exposure.

def make_sydent(test_config={}):
    # CWE-20: Improper Input Validation
    # The test_config dictionary is directly used without validation.
    # An attacker might pass unexpected types that cause errors or unexpected behavior.

    if 'db' not in test_config:
        test_config['db'] = {'db.file': ':memory:'}
    else:
        test_config['db'].setdefault('db.file', ':memory:')

    reactor = MemoryReactorClock()
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config))


@attr.s
class FakeChannel(object):
    # CWE-209: Information Exposure Through Error Messages
    # Detailed exceptions could expose stack traces or sensitive information.
    # Consider sanitizing exception messages.

    site = attr.ib(type=Site)
    _reactor = attr.ib()
    result = attr.ib(default=attr.Factory(dict))
    _producer = None

    @property
    def json_body(self):
        if not self.result:
            raise Exception("No result yet.")
            # CWE-209: Information Exposure Through Error Messages
            # Throwing a generic exception without context can expose internal details.
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
        # CWE-209: Information Exposure Through Error Messages
        # Assertion error messages might expose internal state to an attacker.

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
        # CWE-200: Information Exposure
        # Returning the peer certificate without restrictions could expose sensitive data.
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    # CWE-285: Improper Authorization
    # The class is a placeholder and lacks implementation details, potentially leading to missing authorization checks.
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
    # No validation on 'method', 'path', 'content', and 'access_token'.
    # Malformed inputs could lead to unexpected behavior or crashes.
    
    if not isinstance(method, bytes):
        method = method.encode("ascii")

    if not isinstance(path, bytes):
        path = path.encode("ascii")

    if (
        shorthand
        and not path.startswith(b"/_matrix")
    ):
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
        req.requestHeaders.addRawHeader(
            b"Authorization", b"Bearer " + access_token.encode("ascii")
        )
        # CWE-287: Improper Authentication
        # The use of an access token without validation could allow unauthorized access.

    if federation_auth_origin is not None:
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )
        # CWE-287: Improper Authentication
        # Federation origin usage without validation could be exploited to bypass authentication.

    if content:
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")

    req.requestReceived(method, path, b"1.1")
    # CWE-89: SQL Injection
    # If 'path' or 'content' are used in database queries without sanitization or parameterization, it could lead to SQL injection.

    return req, channel


class ToTwistedHandler(logging.Handler):
    # CWE-532: Information Exposure Through Log Files
    # Logging potentially sensitive information without filtering or encryption can lead to information leakage.
    
    tx_log = twisted.logger.Logger()

    def emit(self, record):
        log_entry = self.format(record)
        log_level = record.levelname.lower().replace("warning", "warn")
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    # CWE-16: Configuration
    # The logging level is set based on an environment variable without validation.
    # An incorrect log level configuration could lead to excessive logging or lack of critical logs.
    
    root_logger = logging.getLogger()

    log_format = (
        "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s"
        " - %(message)s"
    )

    handler = ToTwistedHandler()
    formatter = logging.Formatter(log_format)
    handler.setFormatter(formatter)
    root_logger.addHandler(handler)

    log_level = os.environ.get("SYDENT_TEST_LOG_LEVEL", "ERROR")
    root_logger.setLevel(log_level)


setup_logging()