from htmlnode import HTMLNode

def test_props_to_html_empty():
    node = HTMLNode()
    assert node.props_to_html() == ""

def test_props_to_html_one_prop():
    node = HTMLNode(props={"href": "https://example.com"})
    assert node.props_to_html() == ' href="https://example.com"'

def test_props_to_html_multiple_props():
    node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
    assert ' href="https://example.com"' in node.props_to_html()
    assert ' target="_blank"' in node.props_to_html()

if __name__ == "__main__":
    test_props_to_html_empty()
    test_props_to_html_one_prop()
    test_props_to_html_multiple_props()
    print("All tests passed!")
    
