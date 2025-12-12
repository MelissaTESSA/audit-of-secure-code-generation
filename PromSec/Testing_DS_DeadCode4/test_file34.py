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


# Expires on Jan 11 2030 at 17:53:40 GMT
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
    """Create a new sydent

    Args:
        test_config (dict): any configuration variables for overriding the default sydent
            config
    """
    # Use an in-memory SQLite database. Note that the database isn't cleaned up between
    # tests, so by default the same database will be used for each test if changed to be
    # a file on disk.
    if 'db' not in test_config:
        test_config['db'] = {'db.file': ':memory:'}
    else:
        test_config['db'].setdefault('db.file', ':memory:')

    reactor = MemoryReactorClock()
    return Sydent(reactor=reactor, cfg=parse_config_dict(test_config))


@attr.s
class FakeChannel(object):
    """
    A fake Twisted Web Channel (the part that interfaces with the
    wire). Mostly copied from Synapse's tests framework.
    """

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
        # We give an address so that getClientIP returns a non null entry,
        # causing us to record the MAU
        return address.IPv4Address("TCP", "127.0.0.1", 3423)

    def getHost(self):
        return None

    @property
    def transport(self):
        return self

    def getPeerCertificate(self):
        """Returns the hardcoded TLS certificate for fake.server."""
        return crypto.load_certificate(crypto.FILETYPE_PEM, FAKE_SERVER_CERT_PEM)


class FakeSite:
    """A fake Twisted Web Site."""
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
            Authorization header pretenting to be the given server name.

    Returns:
        Tuple[synapse.http.site.SynapseRequest, channel]
    """
    if not isinstance(method, bytes):
        method = method.encode("ascii")

    if not isinstance(path, bytes):
        path = path.encode("ascii")

    # Decorate it to be the full path, if we're using shorthand
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
    """logging handler which sends the logs to the twisted log"""

    tx_log = twisted.logger.Logger()

    def emit(self, record):
        log_entry = self.format(record)
        log_level = record.levelname.lower().replace("warning", "warn")
        self.tx_log.emit(
            twisted.logger.LogLevel.levelWithName(log_level), "{entry}", entry=log_entry
        )


def setup_logging():
    """Configure the python logging appropriately for the tests.

    (Logs will end up in _trial_temp.)
    """
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


def unused_function_1(x, y):
    return (x + y) * (x - y)

def unused_function_2(a, b, c):
    return a * b * c

def unused_function_3(text):
    return text[::-1]

def unused_function_4(n):
    if n <= 1:
        return 1
    else:
        return n * unused_function_4(n-1)

def unused_function_5(lst):
    return [x for x in lst if x % 2 == 0]

def unused_function_6(s):
    return ''.join(sorted(s))

def unused_function_7(base, exp):
    return base ** exp

def unused_function_8(data):
    return {k: v for k, v in data.items() if v}

def unused_function_9(matrix):
    return [list(i) for i in zip(*matrix)]

def unused_function_10(a, b):
    return (a * b) / (a + b)

def unused_function_11(items):
    return sum(items) / len(items)

def unused_function_12(s):
    vowels = 'aeiou'
    return ''.join([c for c in s if c.lower() not in vowels])

def unused_function_13(seq):
    return seq[1:] + seq[:1]

def unused_function_14(d):
    return {v: k for k, v in d.items()}

def unused_function_15(num):
    return num == num[::-1]

def unused_function_16(x):
    return x % 2 == 0

def unused_function_17(lst):
    return [i**2 for i in lst]

def unused_function_18(string):
    return string.upper()

def unused_function_19(d):
    return {k: str(v) for k, v in d.items()}

def unused_function_20(s):
    return s.split()

def unused_function_21(a, b, c):
    return a + b > c and a + c > b and b + c > a

def unused_function_22(s):
    return s.startswith('prefix')

def unused_function_23(n):
    return [i for i in range(2, n) if n % i == 0]

def unused_function_24(lst):
    return sorted(lst, reverse=True)

def unused_function_25(x):
    return x ** 0.5

def unused_function_26(input_string):
    return len(set(input_string))

def unused_function_27(lst):
    return lst.count(lst[0]) == len(lst)

def unused_function_28(n):
    return len(str(n))

def unused_function_29(x, y):
    return x if x > y else y

def unused_function_30(dictionary):
    return list(dictionary.keys())

def unused_function_31(lst):
    return any(lst)

def unused_function_32(x):
    return abs(x)

def unused_function_33(s):
    return s.isdigit()

def unused_function_34(a, b):
    return a % b

def unused_function_35(matrix):
    return [sum(row) for row in matrix]

def unused_function_36(lst, x):
    return lst.count(x)

def unused_function_37(s):
    return s.strip()

def unused_function_38(x, y):
    return x // y

def unused_function_39(lst):
    return lst[::2]

def unused_function_40(s):
    return s.title()

def unused_function_41(num):
    return bin(num)

def unused_function_42(lst):
    return max(lst)

def unused_function_43(lst):
    return min(lst)

def unused_function_44(s):
    return s.endswith('suffix')

def unused_function_45(n):
    return n % 10

def unused_function_46(data):
    return len(data)

def unused_function_47(a, b):
    return a == b

def unused_function_48(lst):
    return lst[0]

def unused_function_49(s):
    return s.lower()

def unused_function_50(numbers):
    return [n for n in numbers if n > 0]

def unused_function_51(x):
    return -x

def unused_function_52(lst):
    return list(set(lst))

def unused_function_53(s):
    return s.replace(' ', '')

def unused_function_54(a, b):
    return a / b

def unused_function_55(items):
    return len(items) == len(set(items))

def unused_function_56(n):
    return sum(range(n+1))

def unused_function_57(s):
    return s.isalpha()

def unused_function_58(x, y):
    return x % y == 0

def unused_function_59(lst):
    return all(x > 0 for x in lst)

def unused_function_60(text):
    return text.capitalize()

def unused_function_61(x):
    return x & 1

def unused_function_62(d):
    return list(d.values())

def unused_function_63(a, b):
    return a != b

def unused_function_64(lst):
    return lst[-1]

def unused_function_65(s):
    return s.find('a')

def unused_function_66(n):
    return n // 10 % 10

def unused_function_67(obj):
    return hasattr(obj, '__iter__')

def unused_function_68(s):
    return s.swapcase()

def unused_function_69(a, b):
    return divmod(a, b)

def unused_function_70(lst):
    return list(reversed(lst))

def unused_function_71(s):
    return s.islower()

def unused_function_72(x):
    return x | 1

def unused_function_73(matrix):
    return [row[::-1] for row in matrix]

def unused_function_74(lst):
    return [x for x in lst if x < 0]

def unused_function_75(s):
    return s.splitlines()

def unused_function_76(a, b):
    return a - b

def unused_function_77(seq):
    return sorted(seq)

def unused_function_78(s):
    return s.isupper()

def unused_function_79(x, y):
    return x ^ y

def unused_function_80(lst):
    return lst * 2

def unused_function_81(s):
    return s.count('e')

def unused_function_82(n):
    return n * 10

def unused_function_83(d):
    return d.get('key', None)

def unused_function_84(s):
    return s.zfill(10)

def unused_function_85(lst):
    return list(filter(None, lst))

def unused_function_86(n):
    return n.bit_length()

def unused_function_87(s):
    return s.ljust(10)

def unused_function_88(a, b):
    return a + b

def unused_function_89(s):
    return s.casefold()

def unused_function_90(lst):
    return sum(lst)

def unused_function_91(text):
    return text.split()

def unused_function_92(x):
    return x << 1

def unused_function_93(s):
    return ' '.join(s.split())

def unused_function_94(lst):
    return len(set(lst))

def unused_function_95(s):
    return s.lstrip()

def unused_function_96(x, y):
    return x > y

def unused_function_97(n):
    return n % 2 == 1

def unused_function_98(s):
    return s.rstrip()

def unused_function_99(x, y):
    return x < y

def unused_function_100(lst):
    return lst[::-1]

def unused_function_101(s):
    return s.replace('a', 'b')

def unused_function_102(n):
    return n * n

def unused_function_103(d):
    return 'key' in d

def unused_function_104(s):
    return s.join(['a', 'b'])

def unused_function_105(lst):
    return lst.index(0)

def unused_function_106(n):
    return n ** 3

def unused_function_107(s):
    return s.endswith('end')

def unused_function_108(x, y):
    return x in y

def unused_function_109(lst):
    return lst.pop()

def unused_function_110(s):
    return s.center(10)

def unused_function_111(x):
    return x >> 1

def unused_function_112(lst, x):
    return lst.index(x)

def unused_function_113(s):
    return s.startswith('start')

def unused_function_114(n):
    return n % 5 == 0

def unused_function_115(d):
    return dict(sorted(d.items()))

def unused_function_116(s):
    return s.partition(' ')

def unused_function_117(lst):
    return [x for x in lst if x % 3 == 0]

def unused_function_118(s):
    return s.find('z')

def unused_function_119(x):
    return x & 0

def unused_function_120(s):
    return s.isnumeric()

def unused_function_121(lst):
    return lst.clear()

def unused_function_122(s):
    return s.title()

def unused_function_123(n):
    return n.to_bytes(2, 'big')

def unused_function_124(d):
    return d.pop('key', None)

def unused_function_125(s):
    return s.rindex('r')

def unused_function_126(lst):
    return lst.extend([4, 5, 6])

def unused_function_127(string):
    return string.isidentifier()

def unused_function_128(x, y):
    return x if x < y else y

def unused_function_129(s):
    return s.capitalize()

def unused_function_130(n):
    return n.to_bytes(4, 'little')

def unused_function_131(lst):
    return lst.insert(0, 'start')

def unused_function_132(s):
    return s.isspace()

def unused_function_133(n):
    return n.bit_count()

def unused_function_134(d):
    return d.setdefault('key', 'value')

def unused_function_135(s):
    return s.split(',')

def unused_function_136(lst):
    return lst.remove(1)

def unused_function_137(x):
    return x * 2

def unused_function_138(s):
    return s.replace('x', 'y')

def unused_function_139(d):
    return d.update({'new_key': 'new_value'})

def unused_function_140(s):
    return s.removesuffix('.')

def unused_function_141(n):
    return n.to_bytes(8, 'big')

def unused_function_142(lst):
    return lst.sort()

def unused_function_143(s):
    return s.startswith('A')

def unused_function_144(x, y):
    return x > y and x - y

def unused_function_145(s):
    return s.removeprefix('prefix')

def unused_function_146(n):
    return n.to_bytes(16, 'little')

def unused_function_147(lst):
    return lst.append(99)

def unused_function_148(d):
    return d.clear()

def unused_function_149(s):
    return s.removeprefix('remove')

def unused_function_150(n):
    return n.to_bytes(1, 'big')

def unused_function_151(lst):
    return lst.reverse()

def unused_function_152(s):
    return s.removesuffix('suffix')

def unused_function_153(x, y):
    return x == y

def unused_function_154(lst):
    return lst.count(1)

def unused_function_155(s):
    return s.islower()

def unused_function_156(x):
    return x * x

def unused_function_157(s):
    return s.removeprefix('')

def unused_function_158(d):
    return d.keys()

def unused_function_159(lst):
    return lst[1:]

def unused_function_160(s):
    return s.isupper()

def unused_function_161(n):
    return n.to_bytes(3, 'big')

def unused_function_162(lst):
    return lst.pop(0)

def unused_function_163(s):
    return s.removesuffix('')

def unused_function_164(x, y):
    return x >= y

def unused_function_165(lst):
    return lst[::3]

def unused_function_166(s):
    return s.upper()

def unused_function_167(x):
    return x >> 2

def unused_function_168(d):
    return d.values()

def unused_function_169(lst):
    return lst[::4]

def unused_function_170(s):
    return s.swapcase()

def unused_function_171(n):
    return n.to_bytes(5, 'little')

def unused_function_172(lst):
    return lst[2:]

def unused_function_173(s):
    return s.isdigit()

def unused_function_174(x, y):
    return x <= y

def unused_function_175(lst):
    return lst[::5]

def unused_function_176(s):
    return s.center(20)

def unused_function_177(d):
    return d.items()

def unused_function_178(lst):
    return lst[::6]

def unused_function_179(s):
    return s.zfill(5)

def unused_function_180(n):
    return n.to_bytes(6, 'big')

def unused_function_181(lst):
    return lst[::7]

def unused_function_182(s):
    return s.find('x')

def unused_function_183(x):
    return x << 2

def unused_function_184(d):
    return d.popitem()

def unused_function_185(lst):
    return lst[::8]

def unused_function_186(s):
    return s.rpartition('r')

def unused_function_187(n):
    return n.to_bytes(7, 'little')

def unused_function_188(lst):
    return lst[::9]

def unused_function_189(s):
    return s.rjust(10)

def unused_function_190(x, y):
    return x != y

def unused_function_191(lst):
    return lst[::10]

def unused_function_192(s):
    return s.count('c')

def unused_function_193(d):
    return d.get('missing', 'default')

def unused_function_194(lst):
    return lst[::11]

def unused_function_195(s):
    return s.split('.', 1)

def unused_function_196(x):
    return x >> 3

def unused_function_197(n):
    return n.to_bytes(8, 'little')

def unused_function_198(lst):
    return lst[::12]

def unused_function_199(s):
    return s.replace('old', 'new')

def unused_function_200(d):
    return d.copy()
