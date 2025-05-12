from blocktype import (
    markdown_to_html_node,
    block_to_block_type,
    BlockType,
)
import unittest
from textnode import TextNode, TextType
from extracttitle import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_header(self):
        md = """
# This is a header
text in a p
tag here

"""
        self.assertEqual(extract_title(md), "This is a header")

    def test_header_error(self):
        md = """
This is not a header
text in a p
tag here

"""
        with self.assertRaises(Exception):
            extract_title(md)

if __name__ == "__main__":
    unittest.main()