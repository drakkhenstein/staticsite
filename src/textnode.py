from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)
    def __init__(self, text: str, text_type: TextType, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    if not text_node.text:
        return None
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text, {})
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text, {})
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text, {})
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text, {})
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
    else:
        raise Exception(f"Unknown text type")