import unittest
from textnode import TextNode, TextType
from HTMLNode import HTMLNODE, ParentNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_node_container(self):
        child_node = LeafNode("b", "child node")
        parent_prop = {"class" : "container", "id" : "main"}
        parent_node = ParentNode("div", [child_node], parent_prop)
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container" id="main"><b>child node</b></div>'
        )

    def test_parent_with_no_children(self):
        parent = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent.to_html()

    def test_parent_with_no_tag(self):
        parent = ParentNode("p", None)
        with self.assertRaises(ValueError):
            parent.to_html()