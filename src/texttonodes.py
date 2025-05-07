

def text_to_textnodes(text):
    """
    Convert text to a list of TextNode objects.
    """
    from textnode import TextNode, TextType
    from splitnodes import split_nodes_delimiter
    from splitimageslinks import split_nodes_image
    from splitimageslinks import split_nodes_link
    from extractmarkdown import extract_markdown_links
    from extractmarkdown import extract_markdown_images
    from leafnode import LeafNode

    # Split the text into nodes based on the delimiters
    nodes = [TextNode(text, TextType.TEXT)]

    # Split the text into nodes based on the delimiters
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)

    return nodes