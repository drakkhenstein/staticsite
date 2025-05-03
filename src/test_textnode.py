import unittest

from textnode import TextNode, TextType
from textnode import text_node_to_html_node
from leafnode import LeafNode
from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a different text node", TextType.TEXT)
        node4 = TextNode("This is a different text node", TextType.TEXT)
        self.assertEqual(node3, node4)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node6 = TextNode("This is a new node", TextType.TEXT, "https://example.com")
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This is a text node", TextType.LINK)
        node8 = TextNode("This is a text node", TextType.LINK)
        self.assertEqual(node7, node8)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "Bold text")
        self.assertEqual(html_node.props, {})

    def test_italic(self):
        node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "Italic text")
        self.assertEqual(html_node.props, {})

    def test_code(self):
        node = TextNode("Code text", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "Code text")
        self.assertEqual(html_node.props, {})

    def test_link(self):
        node = TextNode("Link text", TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Link text")
        self.assertEqual(html_node.props, {"href": "https://example.com"})

    def test_image(self):
        node = TextNode("Image text", TextType.IMAGE, "https://example.com/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://example.com/image.png", "alt": "Image text"},
        )

    def test_unknown_text_type(self):
        node = TextNode("Unknown text", "unknown")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()