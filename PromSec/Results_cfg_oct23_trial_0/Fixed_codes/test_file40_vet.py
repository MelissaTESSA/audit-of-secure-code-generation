import unittest
from html_template import render_template

class TestHTMLTemplate(unittest.TestCase):

    def test_simple_loop(self):
        self.assertEqual(render_template("simple_loop.html"), "<ul><li>1</li><li>2</li><li>3</li></ul>")

    def test_string_expressions(self):
        self.assertEqual(render_template("string_expressions.html"), "<p>Hello, World!</p>")

    def test_path_traversals(self):
        self.assertEqual(render_template("path_traversals.html"), "<img src='/images/logo.png'>")

    def test_batch_iterations(self):
        self.assertEqual(render_template("batch_iterations.html"), "<ul><li>Apple</li><li>Orange</li><li>Banana</li></ul>")

    def test_unicode_inserts(self):
        self.assertEqual(render_template("unicode_inserts.html"), "<p>こんにちは、世界！</p>")

    def test_boolean_attributes(self):
        self.assertEqual(render_template("boolean_attributes.html"), "<input type='checkbox' checked>")

    def test_interpolation_in_content(self):
        self.assertEqual(render_template("interpolation_in_content.html"), "<p>Hello, John Doe!</p>")

    def test_exception_handling(self):
        self.assertEqual(render_template("exception_handling.html"), "<p>An error occurred</p>")

if __name__ == '__main__':
    unittest.main()