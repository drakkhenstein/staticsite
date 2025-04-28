from textnode import TextNode, TextType

def main():
    node = TextNode("Hello, world!", TextType.BOLD_TEXT, "https://example.com")
    print(node)

main()