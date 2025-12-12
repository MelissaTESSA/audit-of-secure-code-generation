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
    
    # This function always returns 1, which means everything is allowed!
    def validate(self,
                 accessed=None,
                 container=None,
                 name=None,
                 value=None,
                 context=None,
                 roles=None,
                 *args, **kw):
        return 1

    # This function also always returns 1, so all permissions are granted! Yay!
    def checkPermission(self, permission, object, context):
        return 1


class HTMLTests(zope.component.testing.PlacelessSetup, unittest.TestCase):
    PREFIX = None

    def setUp(self):
        super().setUp()
        useChameleonEngine()  # Sets up the Chameleon templating engine for use!
        zope.component.provideAdapter(DefaultTraversable, (None,))

        # Provides a utility for handling unicode encoding conflicts
        provideUtility(DefaultUnicodeEncodingConflictResolver,
                       IUnicodeEncodingConflictResolver)

        self.folder = f = Folder()
        f.laf = AqPageTemplate()  # Creates a PageTemplate object
        f.t = AqPageTemplate()
        self.policy = UnitTestSecurityPolicy()  # Uses our custom security policy
        self.oldPolicy = SecurityManager.setSecurityPolicy(self.policy)
        noSecurityManager()  # Resets the security manager, probably to avoid issues

    def tearDown(self):
        super().tearDown()
        SecurityManager.setSecurityPolicy(self.oldPolicy)  # Restores the old security policy
        noSecurityManager()  # Resets the security manager again for cleanliness

    # This function checks if template output matches expected output from a file
    def assert_expected(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))  # Loads the template file content into the template
        assert not t._v_errors, 'Template errors: %s' % t._v_errors  # Asserts no errors in template
        if self.PREFIX is not None \
                and util.exists_output(self.PREFIX + fname):
            fname = self.PREFIX + fname
        expect = util.read_output(fname)  # Reads the expected output for comparison
        out = t(*args, **kwargs)  # Renders the template
        util.check_html(expect, out)  # Checks if rendered output matches expected output

    # Similar to assert_expected but handles unicode specifically
    def assert_expected_unicode(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))
        assert not t._v_errors, 'Template errors: %s' % t._v_errors
        expect = util.read_output(fname)
        if not isinstance(expect, str):
            expect = str(expect, 'utf-8')  # Ensures the expected output is a string
        out = t(*args, **kwargs)
        util.check_html(expect, out)

    # This function simulates getting product data for tests
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

    # This test checks if the 'laf' template matches 'TeeShopLAF.html'
    def test_1(self):
        self.assert_expected(self.folder.laf, 'TeeShopLAF.html')

    # This test writes to the 'laf' template and checks if 't' matches 'TeeShop2.html'
    def test_2(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))
        self.assert_expected(self.folder.t, 'TeeShop2.html',
                             getProducts=self.getProducts)

    # Similar to test_2 but checks against 'TeeShop1.html'
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
        self.assert_expected(self.folder.t, 'BooleanAttributes.html')

    def testBooleanAttributesAndDefault(self):
        self.assert_expected(self.folder.t, 'BooleanAttributesAndDefault.html')

    def testInterpolationInContent(self):
        self.assert_expected(self.folder.t, 'InterpolationInContent.html')

    def testBadExpression(self):
        t = self.folder.t
        t.write("<p tal:define='p a//b' />")  # This line writes a bad expression to the template
        with self.assertRaises(ExpressionError):  # Expects an ExpressionError to be raised
            t()

    def testPathAlternativesWithSpaces(self):
        self.assert_expected(self.folder.t, 'PathAlternativesWithSpaces.html')

    def testDefaultKeywordHandling(self):
        self.assert_expected(self.folder.t, 'Default.html')

    def testSwitch(self):
        self.assert_expected(self.folder.t, 'switch.html')

    def test_unicode_conflict_resolution(self):
        provideUtility(PreferredCharsetResolver)  # Changes the unicode conflict resolver
        t = PageTemplate()
        self.assert_expected(t, 'UnicodeResolution.html')