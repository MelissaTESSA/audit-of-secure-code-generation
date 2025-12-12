import os
import unittest
from zope.component.testing import PlacelessSetup
from my_template_engine import TemplateEngine

class HTMLTests(PlacelessSetup, unittest.TestCase):

    def setUp(self):
        self.engine = TemplateEngine()
        self.engine.setup_security_policy()

    def tearDown(self):
        self.engine.teardown_security_policy()

    def test_1(self):
        result = self.engine.render_template('template1.html')
        self.assertEqual(result, '<html><body>Template 1</body></html>')

    def test_2(self):
        result = self.engine.render_template('template2.html')
        self.assertEqual(result, '<html><body>Template 2</body></html>')

    def test_3(self):
        result = self.engine.render_template('template3.html')
        self.assertEqual(result, '<html><body>Template 3</body></html>')

if __name__ == '__main__':
    unittest.main()