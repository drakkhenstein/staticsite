

def extract_markdown_images(text):
    import re

    # Regular expression to match markdown image syntax
    pattern = r"!\[([^\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)

    return matches

def extract_markdown_links(text):
    import re

    # Regular expression to match markdown link syntax
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)

    return matches
"""
# Manual testing
if __name__ == "__main__":
    # Test image extraction
    text_with_images = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text_with_images))
    
    # Test link extraction
    text_with_links = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text_with_links))
"""