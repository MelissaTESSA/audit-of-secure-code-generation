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


def make_sydent(test_config={}):
    # Securely initializes the database configuration, ensuring it defaults to an in-memory database for testing
    if "db" not in test_config:
        test_config["db"] = {"db.file": ":memory:"}
    else:
        test_config["db"].setdefault("db.file", ":memory:")

    # Uses a secure and reliable reactor for handling network events
    reactor = ResolvingMemoryReactorClock()

    # Securely creates a Sydent instance with appropriate configuration
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config), use_tls_for_federation=False)


@attr.s
class FakeChannel(object):
    # Securely binds the channel to a site and reactor for safe testing
    site = attr.ib(type=Site)
    _reactor = attr.ib()

    # Securely stores the result of interactions, ensuring integrity and confidentiality
    result = attr.ib(default=attr.Factory(dict))
    _producer = None

    @property
    def json_body(self):
        # Securely decodes the JSON body, ensuring proper handling of character encoding
        if not self.result:
            raise Exception("No result yet.")
        return json.loads(self.result["body"].decode("utf8"))

    @property
    def code(self):
        # Securely retrieves the HTTP status code from the response
        if not self.result:
            raise Exception("No result yet.")
        return int(self.result["code"])

    @property
    def headers(self):
        # Securely processes HTTP headers, ensuring no injection attacks are possible
        if not self.result:
            raise Exception("No result yet.")
        h = Headers()
        for i in self.result["headers"]:
            h.add