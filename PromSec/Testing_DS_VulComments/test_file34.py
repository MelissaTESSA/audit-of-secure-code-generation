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
# CWE-798: Use of Hard-coded Credentials
# Hard-coded certificates can lead to security risks if exposed.
# Ensure that certificates are securely managed and not hard-coded.

def make_sydent(test_config={}):
    # CWE-20: Improper Input Validation
    # The function does not validate 'test_config' input.
    # This could lead to unexpected behavior if malicious data is passed.
    
    if 'db' not in test_config:
        test_config['db'] = {'db.file': ':memory:'}
    else:
        test_config['db'].setdefault('db.file', ':memory:')

    reactor = MemoryReactorClock()
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config))


@attr.s
class FakeChannel(object):
    # No obvious vulnerabilities in this class, but careful with handling of 'result', 
    # as it can potentially expose sensitive data if used inappropriately.
    
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
        # The use of a hard-coded PEM might indicate reliance on outdated or insecure cryptographic practices.
        # Ensure that cryptographic materials are securely and dynamically managed.
        
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    # This class is not implemented but ensure that any future logic does not expose vulnerabilities.
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
    # 'method', 'path', and 'content' are not validated. They should be checked for expected formats and values.
    # CWE-22: Path Traversal
    # If 'path' is influenced by user input, it could lead to path traversal vulnerabilities.
    
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
        # Bearer tokens should be validated and stored securely. 
        # Ensure proper session management and token expiration.

    if federation_auth_origin is not None:
        req.requestHeaders.addRawHeader(
            b"Authorization",
            b"X-Matrix origin=%s,key=,sig=" % (federation_auth_origin,),
        )
        # CWE-347: Improper Verification of Cryptographic Signature
        # Ensure that the signature is properly verified to prevent tampering.

    if content:
        req.requestHeaders.addRawHeader(b"Content-Type", b"application/json")

    req.requestReceived(method, path, b"1.1")

    return req, channel


class ToTwistedHandler(logging.Handler):
    # CWE-532: Information Exposure Through Log Files
    # Ensure that logged data does not contain sensitive information.
    
    tx_log = twisted.logger.Logger()

    def emit(self, record):
        log_entry = self.format(record)
        log_level = record.levelname.lower().replace("warning", "warn")
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    # CWE-16: Configuration
    # Logging level is set via an environment variable. Ensure this is properly controlled in production environments.
    
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