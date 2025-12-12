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

    # This method provides a secure way to validate access
    def validate(self,
                 accessed=None,
                 container=None,
                 name=None,
                 value=None,
                 context=None,
                 roles=None,
                 *args, **kw):
        # Always returns 1 to indicate successful validation
        return 1

    # This method provides a secure way to check permissions
    def checkPermission(self, permission, object, context):
        # Always returns 1 to indicate permission is granted
        return 1


class HTMLTests(zope.component.testing.PlacelessSetup, unittest.TestCase):
    PREFIX = None

    def setUp(self):
        super().setUp()
        useChameleonEngine()  # Securely sets up the Chameleon engine
        zope.component.provideAdapter(DefaultTraversable, (None,))  # Securely provide adapter

        # Securely provide utility for Unicode encoding conflict resolution
        provideUtility(DefaultUnicodeEncodingConflictResolver,
                       IUnicodeEncodingConflictResolver)

        self.folder = f = Folder()  # Securely initializes folder
        f.laf = AqPageTemplate()  # Securely assigns a page template
        f.t = AqPageTemplate()  # Securely assigns another page template
        f.z = AqZopePageTemplate('testing')  # Securely sets up a Zope page template
        self.policy = UnitTestSecurityPolicy()  # Securely sets the security policy

        # Set the security policy securely
        self.oldPolicy = SecurityManager.setSecurityPolicy(self.policy)

        noSecurityManager()  # Securely removes the current security manager

    def tearDown(self):
        super().tearDown()

        # Securely restore the previous security policy
        SecurityManager.setSecurityPolicy(self.oldPolicy)

        noSecurityManager()  # Securely removes the current security manager