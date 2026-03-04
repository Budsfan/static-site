import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
        node3 = TextNode("This is also a test node", TextType.ITALIC_TEXT)
        node4 = TextNode("But is this a test node?", TextType.LINK, "https://www.google.com")
        self.assertNotEqual(node3, node4)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bolt_text(self):
        node = TextNode("Here's some text", TextType.BOLD_TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Here's some text")

    def test_image(self):
        node = TextNode("It's a picture of a dog", TextType.IMAGE, "https://www.google.com/dog")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.props, {'src': 'https://www.google.com/dog', 'alt': "It's a picture of a dog"})
        self.assertEqual(html_node.value, '')
    
    def test_link(self):
        node = TextNode("Link to my myspace page", TextType.LINK, "https://www.myspace.com/mypage")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link to my myspace page")
        self.assertEqual(html_node.props, {'href': 'https://www.myspace.com/mypage'})

    def test_invalid_type(self):
        with self.assertRaises(Exception):
            node = TextNode("words", "bold")
            html_node = text_node_to_html_node(node)
if __name__ == "__main__":
    unittest.main()

