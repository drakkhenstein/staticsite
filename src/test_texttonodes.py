import unittest


class TestTextToTextNodes(unittest.TestCase):
    def test_text_to_textnodes(self):
        # Import necessary modules
        from textnode import TextNode, TextType
        from texttonodes import text_to_textnodes
        from splitnodes import split_nodes_delimiter
        from splitimageslinks import split_nodes_image
        from splitimageslinks import split_nodes_link
        from extractmarkdown import extract_markdown_links
        from extractmarkdown import extract_markdown_images
    
        # Test case 1: Simple text with bold
        text1 = "This is **bold** text"
        expected1 = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        result1 = text_to_textnodes(text1)
        assert len(result1) == len(expected1), f"Expected {len(expected1)} nodes, got {len(result1)}"
        for i in range(len(result1)):
            assert result1[i].text == expected1[i].text, f"Node {i} text doesn't match"
            assert result1[i].text_type == expected1[i].text_type, f"Node {i} type doesn't match"
    
        # Test case 2: Text with multiple formatting
        text2 = "This is **bold** and _italic_ and `code`"
        expected2 = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.TEXT),
            TextNode("code", TextType.CODE)
        ]
        result2 = text_to_textnodes(text2)
        assert len(result2) == len(expected2), f"Expected {len(expected2)} nodes, got {len(result2)}"
        for i in range(len(result2)):
            assert result2[i].text == expected2[i].text, f"Node {i} text doesn't match"
            assert result2[i].text_type == expected2[i].text_type, f"Node {i} type doesn't match"
    
        # Test case 3: Text with image and link
        text3 = "Check out this ![image](https://example.com/image.jpg) and [this link](https://example.com)"
        expected3 = [
            TextNode("Check out this ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.jpg"),
            TextNode(" and ", TextType.TEXT),
            TextNode("this link", TextType.LINK, "https://example.com")
        ]
        result3 = text_to_textnodes(text3)
        assert len(result3) == len(expected3), f"Expected {len(expected3)} nodes, got {len(result3)}"
        for i in range(len(result3)):
            assert result3[i].text == expected3[i].text, f"Node {i} text doesn't match"
            assert result3[i].text_type == expected3[i].text_type, f"Node {i} type doesn't match"
            if result3[i].text_type in [TextType.LINK, TextType.IMAGE]:
                assert result3[i].url == expected3[i].url, f"Node {i} url doesn't match"

if __name__ == "__main__":
    unittest.main()