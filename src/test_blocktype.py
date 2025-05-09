import unittest

from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode
from splitnodes import split_nodes_delimiter
from splitimageslinks import split_nodes_image
from splitimageslinks import split_nodes_link
from extractmarkdown import extract_markdown_links
from extractmarkdown import extract_markdown_images
from markdowntoblocks import markdown_to_blocks
from blocktype import BlockType
from blocktype import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        block =  "### This is a heading paragraph" 
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    def test_paragraph(self):
        block =  "This is a paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_quote(self):
        block =  "> This is a quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_code(self):
        block =  "```python\nprint('Hello, World!')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_unordered_list(self):
        block =  "- Item1\n- Item 2\n- Item 3"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    def test_ordered_list(self):
        block =  "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

if __name__ == "__main__":
    unittest.main()

