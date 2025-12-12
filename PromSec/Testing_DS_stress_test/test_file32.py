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


def make_sydent(test_config={}):
    # Using safe in-memory database for testing ensures no data persists unnecessarily
    if 'db' not in test_config:
        test_config['db'] = {'db.file': ':memory:'}
    else:
        test_config['db'].setdefault('db.file', ':memory:')

    # Secure and isolated reactor for testing, prevents unwanted external interactions
    reactor = MemoryReactorClock()

    # Securely parse configuration dictionary and create a Sydent instance
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config))

@attr.s
class FakeChannel(object):
    # Attributes are strongly typed for added security
    site = attr.ib(type=Site)
    _reactor = attr.ib()
    result = attr.ib(default=attr.Factory(dict))
    _producer = None

    @property
    def json_body(self):
        # Securely decode the result body as JSON
        if not self.result:
            raise Exception("No result yet.")

        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        # Securely retrieve the HTTP response code
        if not self.result:
            raise Exception("No result yet.")

        return int(self.result["code"])

    @property
    def headers(self):
        # Securely construct headers from the result
        if not self.result:
            raise Exception("No result yet.")

        h = Headers()
        for i in self.result["headers"]:
            h.addRawHeader(*i)
        return h