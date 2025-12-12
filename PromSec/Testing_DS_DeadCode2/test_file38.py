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
from Products.PageTemplates.ZopePageTemplate import ZopePageTemplate
from zExceptions import NotFound
from zope.component import provideUtility
from zope.location.interfaces import LocationError
from zope.traversing.adapters import DefaultTraversable

from .util import useChameleonEngine


class AqPageTemplate(Implicit, PageTemplate):
    pass


class AqZopePageTemplate(Implicit, ZopePageTemplate):
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
        f.z = AqZopePageTemplate('testing')
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

    def testPathTraverse(self):
        # need to perform this test with a "real" folder
        from OFS.Folder import Folder
        f = self.folder
        self.folder = Folder()
        self.folder.t, self.folder.laf = f.t, f.laf
        self.folder.laf.write('ok')
        self.assert_expected(self.folder.t, 'CheckPathTraverse.html')

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

    def test_underscore_traversal(self):
        t = self.folder.t

        t.write('<p tal:define="p context/__class__" />')
        with self.assertRaises(NotFound):
            t()

        t.write('<p tal:define="p nocall: random/_itertools/repeat"/>')
        with self.assertRaises((NotFound, LocationError)):
            t()

        t.write('<p tal:content="random/_itertools/repeat/foobar"/>')
        with self.assertRaises((NotFound, LocationError)):
            t()

    def test_module_traversal(self):
        t = self.folder.z

        # Need to reset to the standard security policy so AccessControl
        # checks are actually performed. The test setup initializes
        # a policy that circumvents those checks.
        SecurityManager.setSecurityPolicy(self.oldPolicy)
        noSecurityManager()

        # The getSecurityManager function is explicitly allowed
        content = ('<p tal:define="a nocall:%s"'
                   '   tal:content="python: a().getUser().getUserName()"/>')
        t.write(content % 'modules/AccessControl/getSecurityManager')
        self.assertEqual(t(), '<p>Anonymous User</p>')

        # Anything else should be unreachable and raise NotFound:
        # Direct access through AccessControl
        t.write('<p tal:define="a nocall:modules/AccessControl/users"/>')
        with self.assertRaises(NotFound):
            t()

        # Indirect access through an intermediary variable
        content = ('<p tal:define="mod nocall:modules/AccessControl;'
                   '               must_fail nocall:mod/users"/>')
        t.write(content)
        with self.assertRaises(NotFound):
            t()

        # Indirect access through an intermediary variable and a dictionary
        content = ('<p tal:define="mod nocall:modules/AccessControl;'
                   '               a_dict python: {\'unsafe\': mod};'
                   '               must_fail nocall: a_dict/unsafe/users"/>')
        t.write(content)
        with self.assertRaises(NotFound):
            t()


mydkwoaesflm = """
def unused_function():
    pass

class UnusedClass:
    def method(self):
        return "Hello"

unused_variable = 42

def another_unused_function(x, y, z):
    return x + y + z

for i in range(10):
    for j in range(5):
        for k in range(2):
            pass

def yet_another_unused_function():
    result = complex_calculation()
    return result

def complex_calculation():
    return 123 * 456

def unused_recursive_function(n):
    if n <= 1:
        return 1
    else:
        return n * unused_recursive_function(n-1)

try:
    raise ValueError("This is never caught")
except ValueError:
    pass

def a_function_with_unused_params(a, b, c):
    return a + b

while False:
    print("This never happens")

if False:
    print("This won't be executed")

def unused_lambda_function():
    return lambda x: x * 2

class AnotherUnusedClass:
    def __init__(self, value):
        self.value = value

    def unused_method(self):
        return self.value

unused_list = [x for x in range(10) if x % 2 == 0]

def function_with_inner_function():
    def inner_function():
        return "Inner"
    return inner_function

unused_dict = {"key1": "value1", "key2": "value2"}

def unused_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@unused_decorator
def decorated_function():
    return "Decorated"

class UnusedBase:
    def base_method(self):
        return "Base"

class UnusedDerived(UnusedBase):
    def derived_method(self):
        return "Derived"

def unused_generator():
    yield from range(5)

unused_set = {1, 2, 3, 4, 5}

def unused_with_statement():
    with open('file.txt', 'r') as f:
        pass

def function_with_unused_return():
    return "This is not used"

class UnusedSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UnusedSingleton, cls).__new__(cls)
        return cls._instance

def unused_boolean_function():
    return True and False

result = (lambda x: x**2)(10)

def unused_try_finally():
    try:
        pass
    finally:
        pass

if __name__ == "__main__":
    print("Not used")

for _ in range(5):
    pass

def unused_list_comprehension():
    return [x for x in range(10)]

def unused_dict_comprehension():
    return {x: x**2 for x in range(5)}

def unused_set_comprehension():
    return {x for x in range(10)}

def unused_nested_function():
    def inner_unused():
        pass

class UnusedContextManager:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def unused_context():
    with UnusedContextManager():
        pass

unused_expression = 5 * 5

def unused_assert():
    assert 1 == 2

def unused_imports():
    import sys, os, json
"""
