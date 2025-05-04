import unittest

from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode
from splitnodes import split_nodes_delimiter

class TestSplitNodeDelimiter(unittest.TestCase):
    def test_split_with_no_delimiter(self):
        node = TextNode("This is a text node", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "This is a text node")
        self.assertEqual(result[0].text_type, TextType.TEXT)

    def test_split_with_delimiter(self):
        node = TextNode("This is a **bold** text node", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " text node")
        self.assertEqual(result[2].text_type, TextType.TEXT)
    """
    def test_split_with_multiple_delimiters(self):
        node = TextNode("This is a **bold** and *italic* text node", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 5)
        self.assertEqual(result[0].text, "This is a ")
        self.assertEqual(result[0].text_type, TextType.TEXT)
        self.assertEqual(result[1].text, "bold")
        self.assertEqual(result[1].text_type, TextType.BOLD)
        self.assertEqual(result[2].text, " and ")
        self.assertEqual(result[2].text_type, TextType.TEXT)
        self.assertEqual(result[3].text, "italic")
        self.assertEqual(result[3].text_type, TextType.ITALIC)
        self.assertEqual(result[4].text, " text node")
        self.assertEqual(result[4].text_type, TextType.TEXT)
    """
    def test_split_with_no_closing_delimiter(self):
        node = TextNode("This is a **bold text node", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_split_with_no_opening_delimiter(self):
        node = TextNode("This is a bold** text node", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_split_with_empty_text(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].text, "")
        self.assertEqual(result[0].text_type, TextType.TEXT)
"""
    def test_split_with_empty_delimiter(self):
        node = TextNode("This is a text node", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "", TextType.BOLD)
"""
if __name__ == "__main__":
    unittest.main()