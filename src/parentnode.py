from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)
        if self.children == None:
            raise ValueError("Parent node has no children")
        self.props = props if props is not None else {}

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node has no tag")
        attrs_str = ""
        if self.props:
            for key, value in self.props.items():
                attrs_str += f' {key}="{value}"'
        children_str = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{attrs_str}>{children_str}</{self.tag}>"
