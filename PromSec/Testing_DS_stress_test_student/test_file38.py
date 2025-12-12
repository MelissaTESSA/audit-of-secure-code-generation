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
    # This is a cool class that extends PageTemplate with some Implicit fun! 
    pass


class AqZopePageTemplate(Implicit, ZopePageTemplate):
    # Another cool class that extends ZopePageTemplate with Implicit magic.
    pass


class Folder(util.Base):
    # This is like a basic folder, but with some extra testing stuff.
    pass


class UnitTestSecurityPolicy:
    # This is my security policy for testing. It always returns 1 for validation and permission checks.
    
    def validate(self,
                 accessed=None,
                 container=None,
                 name=None,
                 value=None,
                 context=None,
                 roles=None,
                 *args, **kw):
        # Always return true for validation checks.
        return 1

    def checkPermission(self, permission, object, context):
        # Always allow permission checks. Yay!
        return 1


class HTMLTests(zope.component.testing.PlacelessSetup, unittest.TestCase):
    PREFIX = None

    def setUp(self):
        # Setting things up for each test. Super important to call super()!
        super().setUp()
        useChameleonEngine()  # Use the Chameleon engine for templates.
        zope.component.provideAdapter(DefaultTraversable, (None,))
        
        # Providing a utility for resolving unicode conflicts. So useful!
        provideUtility(DefaultUnicodeEncodingConflictResolver,
                       IUnicodeEncodingConflictResolver)

        # Making a folder and adding some page templates to it.
        self.folder = f = Folder()
        f.laf = AqPageTemplate()
        f.t = AqPageTemplate()
        f.z = AqZopePageTemplate('testing')
        
        # Set a custom security policy for tests.
        self.policy = UnitTestSecurityPolicy()
        self.oldPolicy = SecurityManager.setSecurityPolicy(self.policy)
        
        # No security manager needed here!
        noSecurityManager()

    def tearDown(self):
        # Cleaning up after each test. Super important!
        super().tearDown()
        SecurityManager.setSecurityPolicy(self.oldPolicy)
        noSecurityManager()

    def assert_expected(self, t, fname, *args, **kwargs):
        # Asserts that the template output matches the expected output.
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        if self.PREFIX is not None \
                and util.exists_output(self.PREFIX + fname):
            fname = self.PREFIX + fname
        expect = util.read_output(fname)
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    def assert_expected_unicode(self, t, fname, *args, **kwargs):
        # Similar to assert_expected but handles unicode.
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        expect = util.read_output(fname)
        if not isinstance(expect, str):
            expect = str(expect, 'utf-8')
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    def getProducts(self):
        # Returns a list of products. Imagine these are real!
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
        # Test to see if the template works with TeeShopLAF.html
        self.assert_expected(self.folder.laf, 'TeeShopLAF.html')

    def test_2(self):
        # Writes to the folder's laf template and tests with TeeShop2.html
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))
        self.assert_expected(self.folder.t, 'TeeShop2.html',
                             getProducts=self.getProducts)

    def test_3(self):
        # Similar to test_2 but uses TeeShop1.html
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))
        self.assert_expected(self.folder.t, 'TeeShop1.html',
                             getProducts=self.getProducts)

    def testSimpleLoop(self):
        # Tests a simple loop template.
        self.assert_expected(self.folder.t, 'Loop1.html')

    def testFancyLoop(self):
        # Tests a fancier loop template.
        self.assert_expected(self.folder.t, 'Loop2.html')

    def testGlobalsShadowLocals(self):
        # Tests global variables shadowing local variables.
        self.assert_expected(self.folder.t, 'GlobalsShadowLocals.html')

    def testStringExpressions(self):
        # Tests string expressions in templates.
        self.assert_expected(self.folder.t, 'StringExpression.html')

    def testReplaceWithNothing(self):
        # Test replacing content with nothing.
        self.assert_expected(self.folder.t, 'CheckNothing.html')

    def testWithXMLHeader(self):
        # Tests templates that include an XML header.
        self.assert_expected(self.folder.t, 'CheckWithXMLHeader.html')

    def testNotExpression(self):
        # Tests the 'not' expression in templates.
        self.assert_expected(self.folder.t, 'CheckNotExpression.html')

    def testPathNothing(self):
        # Tests path expressions that should result in nothing.
        self.assert_expected(self.folder.t, 'CheckPathNothing.html')

    def testPathAlt(self):
        # Tests alternative path expressions.
        self.assert_expected(self.folder.t, 'CheckPathAlt.html')

    def testPathTraverse(self):
        # Tests path traversal in templates.
        from OFS.Folder import Folder
        f = self.folder
        self.folder = Folder()
        self.folder.t, self.folder.laf = f.t, f.laf
        self.folder.laf.write('ok')
        self.assert_expected(self.folder.t, 'CheckPathTraverse.html')

    def testBatchIteration(self):
        # Tests batch iteration in templates.
        self.assert_expected(self.folder.t, 'CheckBatchIteration.html')

    def testUnicodeInserts(self):
        # Tests inserting unicode into templates.
        self.assert_expected_unicode(self.folder.t, 'CheckUnicodeInserts.html')

    def testI18nTranslate(self):
        # Tests internationalization translation in templates.
        self.assert_expected(self.folder.t, 'CheckI18nTranslate.html')

    def testImportOldStyleClass(self):
        # Tests importing old style classes in templates.
        self.assert_expected(self.folder.t, 'CheckImportOldStyleClass.html')

    def testRepeatVariable(self):
        # Tests repeat variables in templates.
        self.assert_expected(self.folder.t, 'RepeatVariable.html')

    def testBooleanAttributes(self):
        # Tests boolean attributes in templates.
        self.assert_expected(self.folder.t, 'BooleanAttributes.html')

    def testBooleanAttributesAndDefault(self):
        # Tests boolean attributes and default values in templates.
        self.assert_expected(self.folder.t, 'BooleanAttributesAndDefault.html')

    def testInterpolationInContent(self):
        # Tests interpolation within content in templates.
        self.assert_expected(self.folder.t, 'InterpolationInContent.html')

    def testBadExpression(self):
        # Tests a bad expression that should raise an error.
        t = self.folder.t
        t.write("<p tal:define='p a//b' />")
        with self.assertRaises(ExpressionError):
            t()

    def testPathAlternativesWithSpaces(self):
        # Tests path alternatives that include spaces.
        self.assert_expected(self.folder.t, 'PathAlternativesWithSpaces.html')

    def testDefaultKeywordHandling(self):
        # Tests handling of default keywords in templates.
        self.assert_expected(self.folder.t, 'Default.html')

    def testSwitch(self):
        # Tests the switch statement in templates.
        self.assert_expected(self.folder.t, 'switch.html')

    def test_unicode_conflict_resolution(self):
        # Tests resolving unicode conflicts.
        provideUtility(PreferredCharsetResolver)
        t = PageTemplate()
        self.assert_expected(t, 'UnicodeResolution.html')

    def test_underscore_traversal(self):
        # Tests traversing paths with underscores in them.
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
        # Tests traversing module paths.
        t = self.folder.z

        SecurityManager.setSecurityPolicy(self.oldPolicy)
        noSecurityManager()

        content = ('<p tal:define="a nocall:%s"'
                   '   tal:content="python: a().getUser().getUserName()"/>')
        t.write(content % 'modules/AccessControl/getSecurityManager')
        self.assertEqual(t(), '<p>Anonymous User</p>')

        t.write('<p tal:define="a nocall:modules/AccessControl/users"/>')
        with self.assertRaises(NotFound):
            t()

        content = ('<p tal:define="mod nocall:modules/AccessControl;'
                   '               must_fail nocall:mod/users"/>')
        t.write(content)
        with self.assertRaises(NotFound):
            t()

        content = ('<p tal:define="mod nocall:modules/AccessControl;'
                   '               a_dict python: {\'unsafe\': mod};'
                   '               must_fail nocall: a_dict/unsafe/users"/>')
        t.write(content)
        with self.assertRaises(NotFound):
            t()