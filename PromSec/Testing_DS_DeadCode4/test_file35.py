##############################################################################
#
# Copyright (c) 2002 Zope Foundation and Contributors.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE
#
##############################################################################

import unittest

from chameleon.exc import ExpressionError

import zope.component.testing
from AccessControl import SecurityManager
from AccessControl.SecurityManagement import noSecurityManager
from Acquisition import Implicit
from Products.PageTemplates.interfaces import IUnicodeEncodingConflictResolver
from Products.PageTemplates.PageTemplate import PageTemplate
from Products.PageTemplates.tests import util
from Products.PageTemplates.unicodeconflictresolver import \
    DefaultUnicodeEncodingConflictResolver
from Products.PageTemplates.unicodeconflictresolver import \
    PreferredCharsetResolver
from zope.component import provideUtility
from zope.traversing.adapters import DefaultTraversable

from .util import useChameleonEngine


class AqPageTemplate(Implicit, PageTemplate):
    pass


class Folder(util.Base):
    pass


class UnitTestSecurityPolicy:
    """
        Stub out the existing security policy for unit testing purposes.
    """
    # Standard SecurityPolicy interface
    def validate(self,
                 accessed=None,
                 container=None,
                 name=None,
                 value=None,
                 context=None,
                 roles=None,
                 *args, **kw):
        return 1

    def checkPermission(self, permission, object, context):
        return 1


class HTMLTests(zope.component.testing.PlacelessSetup, unittest.TestCase):
    PREFIX = None

    def setUp(self):
        super().setUp()
        useChameleonEngine()
        zope.component.provideAdapter(DefaultTraversable, (None,))

        provideUtility(DefaultUnicodeEncodingConflictResolver,
                       IUnicodeEncodingConflictResolver)

        self.folder = f = Folder()
        f.laf = AqPageTemplate()
        f.t = AqPageTemplate()
        self.policy = UnitTestSecurityPolicy()
        self.oldPolicy = SecurityManager.setSecurityPolicy(self.policy)
        noSecurityManager()  # Use the new policy.

    def tearDown(self):
        super().tearDown()
        SecurityManager.setSecurityPolicy(self.oldPolicy)
        noSecurityManager()  # Reset to old policy.

    def assert_expected(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        if self.PREFIX is not None \
                and util.exists_output(self.PREFIX + fname):
            fname = self.PREFIX + fname
        expect = util.read_output(fname)
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    def assert_expected_unicode(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        expect = util.read_output(fname)
        if not isinstance(expect, str):
            expect = str(expect, 'utf-8')
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    def getProducts(self):
        return [
            {'description': 'This is the tee for those who LOVE Zope. '
             'Show your heart on your tee.',
             'price': 12.99, 'image': 'smlatee.jpg'
             },
            {'description': 'This is the tee for Jim Fulton. '
             'He\'s the Zope Pope!',
             'price': 11.99, 'image': 'smpztee.jpg'
             },
        ]

    def test_1(self):
        self.assert_expected(self.folder.laf, 'TeeShopLAF.html')

    def test_2(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop2.html',
                             getProducts=self.getProducts)

    def test_3(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop1.html',
                             getProducts=self.getProducts)

    def testSimpleLoop(self):
        self.assert_expected(self.folder.t, 'Loop1.html')

    def testFancyLoop(self):
        self.assert_expected(self.folder.t, 'Loop2.html')

    def testGlobalsShadowLocals(self):
        self.assert_expected(self.folder.t, 'GlobalsShadowLocals.html')

    def testStringExpressions(self):
        self.assert_expected(self.folder.t, 'StringExpression.html')

    def testReplaceWithNothing(self):
        self.assert_expected(self.folder.t, 'CheckNothing.html')

    def testWithXMLHeader(self):
        self.assert_expected(self.folder.t, 'CheckWithXMLHeader.html')

    def testNotExpression(self):
        self.assert_expected(self.folder.t, 'CheckNotExpression.html')

    def testPathNothing(self):
        self.assert_expected(self.folder.t, 'CheckPathNothing.html')

    def testPathAlt(self):
        self.assert_expected(self.folder.t, 'CheckPathAlt.html')

    def testBatchIteration(self):
        self.assert_expected(self.folder.t, 'CheckBatchIteration.html')

    def testUnicodeInserts(self):
        self.assert_expected_unicode(self.folder.t, 'CheckUnicodeInserts.html')

    def testI18nTranslate(self):
        self.assert_expected(self.folder.t, 'CheckI18nTranslate.html')

    def testImportOldStyleClass(self):
        self.assert_expected(self.folder.t, 'CheckImportOldStyleClass.html')

    def testRepeatVariable(self):
        self.assert_expected(self.folder.t, 'RepeatVariable.html')

    def testBooleanAttributes(self):
        # Test rendering an attribute that should be empty or left out
        # if the value is non-True
        self.assert_expected(self.folder.t, 'BooleanAttributes.html')

    def testBooleanAttributesAndDefault(self):
        # Zope 2.9 and below support the semantics that an HTML
        # "boolean" attribute (e.g. 'selected', 'disabled', etc.) can
        # be used together with 'default'.
        self.assert_expected(self.folder.t, 'BooleanAttributesAndDefault.html')

    def testInterpolationInContent(self):
        # the chameleon template engine supports ``${path}``
        # interpolations not only as part of ``string`` expressions
        # but globally
        self.assert_expected(self.folder.t, 'InterpolationInContent.html')

    def testBadExpression(self):
        t = self.folder.t
        t.write("<p tal:define='p a//b' />")
        with self.assertRaises(ExpressionError):
            t()

    def testPathAlternativesWithSpaces(self):
        self.assert_expected(self.folder.t, 'PathAlternativesWithSpaces.html')

    def testDefaultKeywordHandling(self):
        self.assert_expected(self.folder.t, 'Default.html')

    def testSwitch(self):
        self.assert_expected(self.folder.t, 'switch.html')

    def test_unicode_conflict_resolution(self):
        # override with the more "demanding" resolver
        provideUtility(PreferredCharsetResolver)
        t = PageTemplate()
        self.assert_expected(t, 'UnicodeResolution.html')


def unused_function_1():
    x = 42
    y = x + 8
    return y

def unused_function_2():
    name = "Alice"
    greeting = f"Hello, {name}!"
    return greeting

def unused_function_3():
    items = [1, 2, 3, 4, 5]
    total = sum(items)
    return total

def unused_function_4():
    def inner_function():
        return "Inner value"
    return inner_function()

def unused_function_5():
    x = 10
    for i in range(x):
        pass
    return i

def unused_function_6():
    return max(5, 10, 15)

def unused_function_7():
    x = "foo"
    y = "bar"
    return x + y

def unused_function_8():
    return len("dead code")

def unused_function_9():
    test_list = [1, 2, 3]
    return test_list[::-1]

def unused_function_10():
    return {'key': 'value'}

def unused_function_11():
    return 3.14159 * 2

def unused_function_12():
    return "Python" * 3

def unused_function_13():
    return list(range(10))

def unused_function_14():
    return {1, 2, 3}

def unused_function_15():
    return frozenset([4, 5, 6])

def unused_function_16():
    return (1, 2, 3)

def unused_function_17():
    return "spam".upper()

def unused_function_18():
    return "spam".lower()

def unused_function_19():
    return "spam".capitalize()

def unused_function_20():
    return sorted([3, 1, 2])

def unused_function_21():
    return reversed([1, 2, 3])

def unused_function_22():
    return slice(5, 10, 2)

def unused_function_23():
    return hex(255)

def unused_function_24():
    return bin(255)

def unused_function_25():
    return oct(255)

def unused_function_26():
    return abs(-42)

def unused_function_27():
    return round(3.14159, 2)

def unused_function_28():
    return divmod(10, 3)

def unused_function_29():
    return chr(65)

def unused_function_30():
    return ord('A')

def unused_function_31():
    return isinstance(42, int)

def unused_function_32():
    return issubclass(int, object)

def unused_function_33():
    return all([True, True, False])

def unused_function_34():
    return any([False, False, True])

def unused_function_35():
    return ascii('späm')

def unused_function_36():
    return bool(0)

def unused_function_37():
    return bytearray(b"hello")

def unused_function_38():
    return bytes("hello", "utf-8")

def unused_function_39():
    return callable(print)

def unused_function_40():
    return complex(1, 2)

def unused_function_41():
    return dict(a=1, b=2)

def unused_function_42():
    return enumerate(['a', 'b', 'c'])

def unused_function_43():
    return filter(lambda x: x > 0, [-1, 0, 1])

def unused_function_44():
    return map(lambda x: x * 2, [1, 2, 3])

def unused_function_45():
    return hash('test')

def unused_function_46():
    return id('test')

def unused_function_47():
    return iter([1, 2, 3])

def unused_function_48():
    return len([1, 2, 3])

def unused_function_49():
    return list((1, 2, 3))

def unused_function_50():
    return next(iter([1, 2, 3]))

def unused_function_51():
    return pow(2, 3)

def unused_function_52():
    return repr('test')

def unused_function_53():
    return round(3.5)

def unused_function_54():
    return set([1, 2, 2, 3])

def unused_function_55():
    return sorted(['b', 'a', 'c'])

def unused_function_56():
    return str(123)

def unused_function_57():
    return sum([1, 2, 3])

def unused_function_58():
    return tuple([1, 2, 3])

def unused_function_59():
    return type('test')

def unused_function_60():
    return zip([1, 2, 3], ['a', 'b', 'c'])

def unused_function_61():
    return format(123, '04d')

def unused_function_62():
    return memoryview(b'test')

def unused_function_63():
    return range(5)

def unused_function_64():
    return reversed('hello')

def unused_function_65():
    return slice(5)

def unused_function_66():
    return sorted({3, 1, 2})

def unused_function_67():
    return str.encode('test')

def unused_function_68():
    return str.join('-', ['a', 'b', 'c'])

def unused_function_69():
    return str.split('a-b-c', '-')

def unused_function_70():
    return str.replace('spam', 's', 'h')

def unused_function_71():
    return str.strip(' test ')

def unused_function_72():
    return str.find('test', 'e')

def unused_function_73():
    return "python".islower()

def unused_function_74():
    return "PYTHON".isupper()

def unused_function_75():
    return "Python".istitle()

def unused_function_76():
    return "123".isdigit()

def unused_function_77():
    return "abc".isalpha()

def unused_function_78():
    return "abc123".isalnum()

def unused_function_79():
    return "   ".isspace()

def unused_function_80():
    return "Python".startswith("Py")

def unused_function_81():
    return "Python".endswith("on")

def unused_function_82():
    return "Python".capitalize()

def unused_function_83():
    return "Python".casefold()

def unused_function_84():
    return "Python".center(10)

def unused_function_85():
    return "Python".count("t")

def unused_function_86():
    return "Python".encode()

def unused_function_87():
    return "Python".expandtabs(4)

def unused_function_88():
    return "Python".find("t")

def unused_function_89():
    return "Python".format()

def unused_function_90():
    return "Python".index("t")

def unused_function_91():
    return "Python".isalnum()

def unused_function_92():
    return "Python".isalpha()

def unused_function_93():
    return "Python".isdecimal()

def unused_function_94():
    return "Python".isdigit()

def unused_function_95():
    return "Python".islower()

def unused_function_96():
    return "Python".isnumeric()

def unused_function_97():
    return "Python".isspace()

def unused_function_98():
    return "Python".istitle()

def unused_function_99():
    return "Python".isupper()

def unused_function_100():
    return "Python".join(["a", "b", "c"])

def unused_function_101():
    return "Python".ljust(10)

def unused_function_102():
    return "Python".lower()

def unused_function_103():
    return "Python".lstrip()

def unused_function_104():
    return "Python".partition("t")

def unused_function_105():
    return "Python".replace("Py", "Jy")

def unused_function_106():
    return "Python".rfind("t")

def unused_function_107():
    return "Python".rindex("t")

def unused_function_108():
    return "Python".rjust(10)

def unused_function_109():
    return "Python".rpartition("t")

def unused_function_110():
    return "Python".rsplit()

def unused_function_111():
    return "Python".rstrip()

def unused_function_112():
    return "Python".split()

def unused_function_113():
    return "Python".splitlines()

def unused_function_114():
    return "Python".startswith("P")

def unused_function_115():
    return "Python".strip()

def unused_function_116():
    return "Python".swapcase()

def unused_function_117():
    return "Python".title()

def unused_function_118():
    return "Python".upper()

def unused_function_119():
    return "Python".zfill(10)

def unused_function_120():
    return frozenset({1, 2, 3})

def unused_function_121():
    return bin(256)

def unused_function_122():
    return hex(256)

def unused_function_123():
    return oct(256)

def unused_function_124():
    return abs(-256)

def unused_function_125():
    return divmod(256, 10)

def unused_function_126():
    return chr(97)

def unused_function_127():
    return ord("a")

def unused_function_128():
    return isinstance(256, int)

def unused_function_129():
    return issubclass(int, object)

def unused_function_130():
    return all([True, False, True])

def unused_function_131():
    return any([False, False, True])

def unused_function_132():
    return ascii("äöü")

def unused_function_133():
    return bool(1)

def unused_function_134():
    return bytearray(b"hello world")

def unused_function_135():
    return bytes("hello world", "utf-8")

def unused_function_136():
    return callable(len)

def unused_function_137():
    return complex(2, 3)

def unused_function_138():
    return dict(x=1, y=2)

def unused_function_139():
    return enumerate(['x', 'y', 'z'])

def unused_function_140():
    return filter(lambda x: x > 0, [-2, -1, 0, 1, 2])

def unused_function_141():
    return map(lambda x: x**2, [1, 2, 3])

def unused_function_142():
    return hash('hash this')

def unused_function_143():
    return id('unique id')

def unused_function_144():
    return iter([4, 5, 6])

def unused_function_145():
    return len([4, 5, 6])

def unused_function_146():
    return list((4, 5, 6))

def unused_function_147():
    return next(iter([4, 5, 6]))

def unused_function_148():
    return pow(3, 3)

def unused_function_149():
    return repr('representation')

def unused_function_150():
    return round(4.5678)

def unused_function_151():
    return set([4, 5, 6, 5])

def unused_function_152():
    return sorted(['c', 'a', 'b'])

def unused_function_153():
    return str(456)

def unused_function_154():
    return sum([4, 5, 6])

def unused_function_155():
    return tuple([4, 5, 6])

def unused_function_156():
    return type('type test')

def unused_function_157():
    return zip([4, 5, 6], ['x', 'y', 'z'])

def unused_function_158():
    return format(456, '06d')

def unused_function_159():
    return memoryview(b'hello world')

def unused_function_160():
    return range(10)

def unused_function_161():
    return reversed('hello world')

def unused_function_162():
    return slice(10)

def unused_function_163():
    return sorted({6, 4, 5})

def unused_function_164():
    return str.encode('encode this')

def unused_function_165():
    return str.join(' ', ['join', 'these', 'words'])

def unused_function_166():
    return str.split('split these words')

def unused_function_167():
    return str.replace('replace', 'e', 'a')

def unused_function_168():
    return str.strip(' strip ')

def unused_function_169():
    return str.find('find this', 't')

def unused_function_170():
    return "LOWER".lower()

def unused_function_171():
    return "upper".upper()

def unused_function_172():
    return "title case".title()

def unused_function_173():
    return "12345".isdigit()

def unused_function_174():
    return "letters".isalpha()

def unused_function_175():
    return "word123".isalnum()

def unused_function_176():
    return "    ".isspace()

def unused_function_177():
    return "startswith".startswith("start")

def unused_function_178():
    return "endswith".endswith("with")

def unused_function_179():
    return "capitalize".capitalize()

def unused_function_180():
    return "casefold".casefold()

def unused_function_181():
    return "center".center(10)

def unused_function_182():
    return "count".count("c")

def unused_function_183():
    return "encode".encode()

def unused_function_184():
    return "expandtabs".expandtabs(4)

def unused_function_185():
    return "find".find("f")

def unused_function_186():
    return "format".format()

def unused_function_187():
    return "index".index("i")

def unused_function_188():
    return "isalnum".isalnum()

def unused_function_189():
    return "isalpha".isalpha()

def unused_function_190():
    return "isdecimal".isdecimal()

def unused_function_191():
    return "isdigit".isdigit()

def unused_function_192():
    return "islower".islower()

def unused_function_193():
    return "isnumeric".isnumeric()

def unused_function_194():
    return "isspace".isspace()

def unused_function_195():
    return "istitle".istitle()

def unused_function_196():
    return "isupper".isupper()

def unused_function_197():
    return "join".join(["a", "b", "c"])

def unused_function_198():
    return "ljust".ljust(10)

def unused_function_199():
    return "lower".lower()

def unused_function_200():
    return "lstrip".lstrip()
