from textnode import TextNode, TextType
from htmlnode import HTMLNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        opening_index = text.find(delimiter)
        if opening_index == -1:
            new_nodes.append(old_node)
            continue
        closing_index = text.find(delimiter, opening_index + len(delimiter))
        if closing_index == -1:
            raise ValueError(f"No closing delimiter found for {delimiter}")
        before_text = text[:opening_index]
        between_text = text[opening_index + len(delimiter):closing_index]
        after_text = text[closing_index + len(delimiter):]
        if before_text:
            new_nodes.append(TextNode(before_text, TextType.TEXT))
        new_nodes.append(TextNode(between_text, text_type))
        if after_text:
            remaining_nodes = split_nodes_delimiter([TextNode(after_text, TextType.TEXT)], delimiter, text_type)
            new_nodes.extend(remaining_nodes)
    return new_nodes
