import os
import logging
from twisted.internet import reactor
from sydent.tls import TLSTerminator
from sydent.resolvers.google_dns import GoogleDNSResolver
from sydent.sydent import Sydent

os.environ["SECRET_KEY"] = "my_secret_key"
os.environ["PASSWORD"] = "my_password"

class FakeTLSTerminator(TLSTerminator):
    pass

def fake_resolver():
    return GoogleDNSResolver()

logging.basicConfig(level=logging.DEBUG)

sydent = Sydent(FakeTLSTerminator(), fake_resolver())
reactor.run()