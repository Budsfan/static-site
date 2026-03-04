import unittest

from HTMLNode import HTMLNODE, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

class TestHTMLNodeEdge(unittest.TestCase):
    def test_edge_case(self):
        node = LeafNode(None, "Here's some information")
        self.assertEqual(node.to_html(),"Here's some information")



class TestHTMLNode(unittest.TestCase):
    def test_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_link(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Just some raw text")
        self.assertEqual(node.to_html(), "Just some raw text")
    
