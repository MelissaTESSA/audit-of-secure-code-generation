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


# This class is like a special template with some extra abilities (like magic!)
class AqPageTemplate(Implicit, PageTemplate):
    pass


# Another magic template, but a bit different from AqPageTemplate
class AqZopePageTemplate(Implicit, ZopePageTemplate):
    pass


# A simple folder class to keep things organized
class Folder(util.Base):
    pass


# This is like a pretend security policy for our tests
class UnitTestSecurityPolicy:
    
    # This method always returns true, so everything is "safe"!
    def validate(self,
                 accessed=None,
                 container=None,
                 name=None,
                 value=None,
                 context=None,
                 roles=None,
                 *args, **kw):
        return 1

    # Always allows permission, no matter what!
    def checkPermission(self, permission, object, context):
        return 1


# This is where we write our test cases
class HTMLTests(zope.component.testing.PlacelessSetup, unittest.TestCase):
    PREFIX = None

    # This function sets up everything we need before each test
    def setUp(self):
        super().setUp()
        useChameleonEngine()  # This must be important for templates
        zope.component.provideAdapter(DefaultTraversable, (None,))

        # Providing a utility for handling encoding conflicts
        provideUtility(DefaultUnicodeEncodingConflictResolver,
                       IUnicodeEncodingConflictResolver)

        self.folder = f = Folder()  # Creating our folder to put stuff in
        f.laf = AqPageTemplate()  # Adding a template to the folder
        f.t = AqPageTemplate()  # Another template in the folder
        f.z = AqZopePageTemplate('testing')  # Zope template with a name
        self.policy = UnitTestSecurityPolicy()  # Use our fake security policy
        self.oldPolicy = SecurityManager.setSecurityPolicy(self.policy)  # Save old policy
        noSecurityManager()  # Remove current security manager for now

    # Cleans up after each test
    def tearDown(self):
        super().tearDown()
        SecurityManager.setSecurityPolicy(self.oldPolicy)  # Restore old policy
        noSecurityManager()  # Remove security manager again

    # This function checks if our templates work as expected
    def assert_expected(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))  # Write the input to the template
        assert not t._v_errors, 'Template errors: %s' % t._v_errors  # Check for errors
        if self.PREFIX is not None \
                and util.exists_output(self.PREFIX + fname):
            fname = self.PREFIX + fname
        expect = util.read_output(fname)  # Expected output
        out = t(*args, **kwargs)  # Actual output
        util.check_html(expect, out)  # Compare them

    # Special check for unicode-related tests
    def assert_expected_unicode(self, t, fname, *args, **kwargs):
        t.write(util.read_input(fname))  # Write the input to the template
        assert not t._v_errors, 'Template errors: %s' % t._v_errors  # Check for errors
        expect = util.read_output(fname)  # Expected output
        if not isinstance(expect, str):
            expect = str(expect, 'utf-8')  # Ensure it's a string
        out = t(*args, **kwargs)  # Actual output
        util.check_html(expect, out)  # Compare them

    # A function to get some products info, returns a list of dictionaries
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

    # Our first test, checks a specific template
    def test_1(self):
        self.assert_expected(self.folder.laf, 'TeeShopLAF.html')

    # Another test, checks a second template with products
    def test_2(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop2.html',
                             getProducts=self.getProducts)

    # Yet another test, similar to test_2 but with a different template
    def test_3(self):
        self.folder.laf.write(util.read_input('TeeShopLAF.html'))

        self.assert_expected(self.folder.t, 'TeeShop1.html',
                             getProducts=self.getProducts)

    # Tests simple loops in the template
    def testSimpleLoop(self):
        self.assert_expected(self.folder.t, 'Loop1.html')

    # Tests fancy loops in the template
    def testFancyLoop(self):
        self.assert_expected(self.folder.t, 'Loop2.html')

    # Checks if global variables can shadow local ones
    def testGlobalsShadowLocals(self):
        self.assert_expected(self.folder.t, 'GlobalsShadowLocals.html')

    # Tests string expressions in the template
    def testStringExpressions(self):
        self.assert_expected(self.folder.t, 'StringExpression.html')

    # Checks if template can replace content with nothing
    def testReplaceWithNothing(self):
        self.assert_expected(self.folder.t, 'CheckNothing.html')

    # Tests if template can handle XML headers
    def testWithXMLHeader(self):
        self.assert_expected(self.folder.t, 'CheckWithXMLHeader.html')

    # Tests 'not' expressions in the template
    def testNotExpression(self):
        self.assert_expected(self.folder.t, 'CheckNotExpression.html')

    # Test for path expressions that result in nothing
    def testPathNothing(self):
        self.assert_expected(self.folder.t, 'CheckPathNothing.html')

    # Test for alternative path expressions
    def testPathAlt(self):
        self.assert_expected(self.folder.t, 'CheckPathAlt.html')

    # Tests traversing paths in the template
    def testPathTraverse(self):
        from OFS.Folder import Folder
        f = self.folder
        self.folder = Folder()
        self.folder.t, self.folder.laf = f.t, f.laf
        self.folder.laf.write('ok')
        self.assert_expected(self.folder.t, 'CheckPathTraverse.html')

    # Tests iteration over batches in the template
    def testBatchIteration(self):
        self.assert_expected(self.folder.t, 'CheckBatchIteration.html')

    # Tests insertion of unicode content in the template
    def testUnicodeInserts(self):
        self.assert_expected_unicode(self.folder.t, 'CheckUnicodeInserts.html')

    # Tests internationalization translation in the template
    def testI18nTranslate(self):
        self.assert_expected(self.folder.t, 'CheckI18nTranslate.html')

    # Tests importing an old-style class in the template
    def testImportOldStyleClass(self):
        self.assert_expected(self.folder.t, 'CheckImportOldStyleClass.html')

    # Tests repeat variable functionality in the template
    def testRepeatVariable(self):
        self.assert_expected(self.folder.t, 'RepeatVariable.html')

    # Tests boolean attributes in the template
    def testBooleanAttributes(self):
        self.assert_expected(self.folder.t, 'BooleanAttributes.html')

    # Tests boolean attributes and default values in the template
    def testBooleanAttributesAndDefault(self):
        self.assert_expected(self.folder.t, 'BooleanAttributesAndDefault.html')

    # Tests interpolation in the content of the template
    def testInterpolationInContent(self):
        self.assert_expected(self.folder.t, 'InterpolationInContent.html')

    # Tests handling of bad expressions in the template
    def testBadExpression(self):
        t = self.folder.t
        t.write("<p tal:define='p a//b' />")
        with self.assertRaises(ExpressionError):
            t()

    # Tests path alternatives with spaces in the template
    def testPathAlternativesWithSpaces(self):
        self.assert_expected(self.folder.t, 'PathAlternativesWithSpaces.html')

    # Tests handling of default keyword in the template
    def testDefaultKeywordHandling(self):
        self.assert_expected(self.folder.t, 'Default.html')

    # Tests switch-case like functionality in the template
    def testSwitch(self):
        self.assert_expected(self.folder.t, 'switch.html')

    # Tests resolution of unicode conflicts in the template
    def test_unicode_conflict_resolution(self):
        provideUtility(PreferredCharsetResolver)
        t = PageTemplate()
        self.assert_expected(t, 'UnicodeResolution.html')

    # Tests handling of underscores in path traversal
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

    # Tests module traversal in the template
    def test_module_traversal(self):
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

    # Tests handling of exceptions in the template
    def testHandleException(self):
        t = self.folder.t
        t.write("<p tal:define='p python:1/0' />")
        try:
            t()
        except ZeroDivisionError:
            pass

# This runs all the tests when the script is executed
if __name__ == '__main__':
    unittest.main()