import os
import unittest
from html_render import render_html

class TestHTMLRendering(unittest.TestCase):

    def test_render_html_basic(self):
        html = render_html("<h1>Hello, World!</h1>")
        self.assertEqual(html, "<h1>Hello, World!</h1>")

    def test_render_html_with_attributes(self):
        html = render_html('<a href="https://www.example.com">Click here</a>')
        self.assertEqual(html, '<a href="https://www.example.com">Click here</a>')

    def test_render_html_nested_elements(self):
        html = render_html("<div><p>This is a paragraph</p></div>")
        self.assertEqual(html, "<div><p>This is a paragraph</p></div>")

if __name__ == '__main__':
    unittest.main()