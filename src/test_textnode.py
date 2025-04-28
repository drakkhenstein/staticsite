import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
        node3 = TextNode("This is a different text node", TextType.NORMAL)
        node4 = TextNode("This is a different text node", TextType.NORMAL)
        self.assertEqual(node3, node4)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://example.com")
        node6 = TextNode("This is a new node", TextType.NORMAL, "https://example.com")
        self.assertNotEqual(node5, node6)
        node7 = TextNode("This is a text node", TextType.LINKS)
        node8 = TextNode("This is a text node", TextType.LINKS)
        self.assertEqual(node7, node8)


if __name__ == "__main__":
    unittest.main()