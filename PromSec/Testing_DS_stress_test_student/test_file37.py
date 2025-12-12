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
from zExceptions import NotFound
from zope.component import provideUtility
from zope.traversing.adapters import DefaultTraversable

from .util import useChameleonEngine


class AqPageTemplate(Implicit, PageTemplate):
    pass


class Folder(util.Base):
    pass


class UnitTestSecurityPolicy:
    
    # This method always returns 1, which I guess means everything is valid?
    # Seems like a nice way to avoid permission issues during tests!
    def validate(self,
                 accessed=None,
                 container=None,
                 name=None,
                 value=None,
                 context=None,
                 roles=None,
                 *args, **kw):
        return 1

    # This method always returns 1 too, so I think it means all permissions are granted?
    def checkPermission(self, permission, object, context):
        return 1


# This class is for testing HTML templates
class HTMLTests(zope.component.testing.PlacelessSetup, unittest.TestCase):
    PREFIX = None

    def setUp(self):
        super().setUp()
        useChameleonEngine()  # Sets up the template engine
        zope.component.provideAdapter(DefaultTraversable, (None,))  # Provides a default adapter

        # Provides a utility for handling unicode encoding conflicts
        provideUtility(DefaultUnicodeEncodingConflictResolver,
                       IUnicodeEncodingConflictResolver)

        self.folder = f = Folder()  # Creating a folder to hold templates
        f.laf = AqPageTemplate()  # Adding a template called 'laf'
        f.t = AqPageTemplate()  # Adding another template called 't'
        self.policy = UnitTestSecurityPolicy()  # Using our custom security policy
        self.oldPolicy = SecurityManager.setSecurityPolicy(self.policy)  # Replacing the current security policy
        noSecurityManager()  # Resetting the security manager

    def tearDown(self):
        super().tearDown()
        SecurityManager.setSecurityPolicy(self.oldPolicy)  # Restoring the old security policy
        noSecurityManager()

    # This method checks if the template output matches the expected output
    def assert_expected(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))  # Writing content to the template from a file
        assert not t._v_errors, 'Template errors: %s' % t._v_errors  # Asserting no errors occurred
        if self.PREFIX is not None \
                and util.exists_output(self.PREFIX + fname):
            fname = self.PREFIX + fname
        expect = util.read_output(fname)  # Reading the expected output from a file
        out = t(*args, **kwargs)  # Rendering the template
        util.check_html(expect, out)  # Checking if the rendered HTML matches the expected output

    # This method does the same as assert_expected but for unicode content
    def assert_expected_unicode(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        expect = util.read_output(fname)
        if not isinstance(expect, str):
            expect = str(expect, 'utf-8')
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    # Just a method to return a list of products, might be used in templates
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

    # This test checks a template called 'TeeShopLAF.html'
    def test_1(self):
        self.assert_expected(self.folder.laf, 'TeeShopLAF.html')

    # This test writes and checks 'TeeShopLAF.html' and 'TeeShop2.html'
    def test_2(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop2.html',
                             getProducts=self.getProducts)

    # This test writes and checks 'TeeShopLAF.html' and 'TeeShop1.html'
    def test_3(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop1.html',
                             getProducts=self.getProducts)

    # This test checks a simple loop
    def testSimpleLoop(self):
        self.assert_expected(self.folder.t, 'Loop1.html')

    # This test checks a fancy loop
    def testFancyLoop(self):
        self.assert_expected(self.folder.t, 'Loop2.html')

    # This test checks if globals shadow locals in the template
    def testGlobalsShadowLocals(self):
        self.assert_expected(self.folder.t, 'GlobalsShadowLocals.html')

    # This test checks string expressions in the template
    def testStringExpressions(self):
        self.assert_expected(self.folder.t, 'StringExpression.html')

    # This test checks replacing with nothing in the template
    def testReplaceWithNothing(self):
        self.assert_expected(self.folder.t, 'CheckNothing.html')

    # This test checks templates with an XML header
    def testWithXMLHeader(self):
        self.assert_expected(self.folder.t, 'CheckWithXMLHeader.html')

    # This test checks 'not' expressions in the template
    def testNotExpression(self):
        self.assert_expected(self.folder.t, 'CheckNotExpression.html')

    # This test checks path expressions that lead to nothing
    def testPathNothing(self):
        self.assert_expected(self.folder.t, 'CheckPathNothing.html')

    # This test checks alternative path expressions
    def testPathAlt(self):
        self.assert_expected(self.folder.t, 'CheckPathAlt.html')

    # This test checks path traversal in templates
    def testPathTraverse(self):
        from OFS.Folder import Folder
        f = self.folder
        self.folder = Folder()
        self.folder.t, self.folder.laf = f.t, f.laf
        self.folder.laf.write('ok')
        self.assert_expected(self.folder.t, 'CheckPathTraverse.html')

    # This test checks batch iteration in templates
    def testBatchIteration(self):
        self.assert_expected(self.folder.t, 'CheckBatchIteration.html')

    # This test checks unicode inserts in templates
    def testUnicodeInserts(self):
        self.assert_expected_unicode(self.folder.t, 'CheckUnicodeInserts.html')

    # This test checks internationalization translation in templates
    def testI18nTranslate(self):
        self.assert_expected(self.folder.t, 'CheckI18nTranslate.html')

    # This test checks importing an old-style class in the template
    def testImportOldStyleClass(self):
        self.assert_expected(self.folder.t, 'CheckImportOldStyleClass.html')

    # This test checks the repeat variable in templates
    def testRepeatVariable(self):
        self.assert_expected(self.folder.t, 'RepeatVariable.html')

    # This test checks boolean attributes in templates
    def testBooleanAttributes(self):
        self.assert_expected(self.folder.t, 'BooleanAttributes.html')

    # This test checks boolean attributes and default values in templates
    def testBooleanAttributesAndDefault(self):
        self.assert_expected(self.folder.t, 'BooleanAttributesAndDefault.html')

    # This test checks interpolation in content
    def testInterpolationInContent(self):
        self.assert_expected(self.folder.t, 'InterpolationInContent.html')

    # This test checks if a bad expression raises an error
    def testBadExpression(self):
        t = self.folder.t
        t.write("<p tal:define='p a//b' />")
        with self.assertRaises(ExpressionError):
            t()

    # This test checks path alternatives with spaces
    def testPathAlternativesWithSpaces(self):
        self.assert_expected(self.folder.t, 'PathAlternativesWithSpaces.html')

    # This test checks default keyword handling in templates
    def testDefaultKeywordHandling(self):
        self.assert_expected(self.folder.t, 'Default.html')

    # This test checks the 'switch' statement in templates
    def testSwitch(self):
        self.assert_expected(self.folder.t, 'switch.html')

    # This test checks unicode conflict resolution
    def test_unicode_conflict_resolution(self):
        provideUtility(PreferredCharsetResolver)
        t = PageTemplate()
        self.assert_expected(t, 'UnicodeResolution.html')

    # This test checks underscore traversal in templates
    def test_underscore_traversal(self):
        t = self.folder.t

        t.write('<p tal:define="p context/__class__" />')
        with self.assertRaises(NotFound):
            t()

        t.write('<p tal:define="p nocall: random/_itertools/repeat"/>')
        with self.assertRaises(NotFound):
            t()

        t.write('<p tal:content="random/_itertools/repeat/foobar"/>')
        with self.assertRaises(NotFound):
            t()