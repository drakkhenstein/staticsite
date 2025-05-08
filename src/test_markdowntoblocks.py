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

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md ="""
This is a **bolded** paragraph

This is a paragraph with _italic text_ and 'code' here.
This is another paragraph on a new line.

- This is a list item
- This is another list item
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a **bolded** paragraph",
                "This is a paragraph with _italic text_ and 'code' here.\nThis is another paragraph on a new line.",
                "- This is a list item\n- This is another list item",
            ],
        )

if __name__ == "__main__":
    unittest.main()