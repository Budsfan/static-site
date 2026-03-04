import unittest
from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        text = "I am writing some text here"
        self.assertEqual(block_to_block_type(text), BlockType.PARAGRAPH)
    def test_heading(self):
        text = "###### This is a heading"
        self.assertEqual(block_to_block_type(text), BlockType.HEADING)
    def test_quote(self):
        text = ">This is a quote"
        self.assertEqual(block_to_block_type(text), BlockType.QUOTE)
    def test_code(self):
        text = "```these are lines of code```"
        self.assertEqual(block_to_block_type(text), BlockType.CODE)
    def test_unordered_list(self):
        text = """-thing
        -another thing
        -an additional thing"""
        self.assertEqual(block_to_block_type(text), BlockType.UNORDERED_LIST)
    def test_ordered_list(self):
        text = """1.first thing
        2. second thing
        3. third thing"""
        self.assertEqual(block_to_block_type(text), BlockType.ORDERED_LIST)