import unittest
from node_splitter import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextType, TextNode


class TestNodeSplitter(unittest.TestCase):
    def test_node_splitter(self):
        nodes = [TextNode("**some of this string** is bold and some of it is not", TextType.TEXT)]
        new_node = split_nodes_delimiter(nodes, '**', TextType.BOLD_TEXT)
        self.assertEqual(new_node, [TextNode('some of this string', TextType.BOLD_TEXT),
                                    TextNode(" is bold and some of it is not" , TextType.TEXT),
                                    ]
                                    )
    def test_with_alternating_types(self):
        nodes = [TextNode("**It's** beginning", TextType.TEXT),
                 TextNode("to look **a lot**", TextType.TEXT),
                 TextNode("like Christmas... **and some bold text**", TextType.TEXT)
                 ]
        new_nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD_TEXT)
        self.assertEqual(new_nodes, [TextNode("It's", TextType.BOLD_TEXT),
                                     TextNode(" beginning", TextType.TEXT),
                                     TextNode("to look ", TextType.TEXT),
                                     TextNode("a lot", TextType.BOLD_TEXT),
                                     TextNode("like Christmas... ", TextType.TEXT),
                                     TextNode("and some bold text", TextType.BOLD_TEXT)])
        
    def test_italics(self):
        nodes = [TextNode("There are some _small words_ in this sentence", TextType.TEXT)]
        new_nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC_TEXT)
        self.assertEqual(new_nodes, [TextNode("There are some ", TextType.TEXT),
                                     TextNode("small words", TextType.ITALIC_TEXT),
                                     TextNode(" in this sentence", TextType.TEXT)])
        



class TextPropExtractor(unittest.TestCase):
    def test_link_extractor(self):
        link_text_string = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        tuples = extract_markdown_links(link_text_string)
        self.assertEqual(tuples, [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')])

    def test_image_extractor(self):
        image_test_string = """
Here is one image:
![dragon](https://i.imgur.com/zjjcJKZ.png)

Here is another:
![orc-warrior](https://i.imgur.com/abc1234.jpg)

Some random text in between.

![fireball spell](https://i.imgur.com/fire987.gif)

And one more for good measure:
![healing_potion](https://i.imgur.com/potion456.png)

End of string.
"""
        tuples = extract_markdown_images(image_test_string)
        self.assertEqual(tuples, [('dragon', 'https://i.imgur.com/zjjcJKZ.png'), ('orc-warrior', 'https://i.imgur.com/abc1234.jpg'), ('fireball spell', 'https://i.imgur.com/fire987.gif'), ('healing_potion', 'https://i.imgur.com/potion456.png')])

class Test_Split_Nodes(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )
    
    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to google](https://www.google.com) and another [to facebook](https://www.facebook.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to google", TextType.LINK, "https://www.google.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "to facebook", TextType.LINK, "https://www.facebook.com"
                ),
            ],
            new_nodes,
        )
class Test_Text_To_Textnodes(unittest.TestCase):
    def test_text_to_textnode(self):
        node = TextNode("This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)", TextType.TEXT)
        new_nodes = text_to_textnodes([node])
        self.assertEqual(new_nodes, [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD_TEXT),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC_TEXT),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE_TEXT),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
    ])
