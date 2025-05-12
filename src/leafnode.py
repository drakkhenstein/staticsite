from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, children=None, props=props)
        self.value = value
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node has no value")
        if self.tag is None:
            return self.value
        attrs_str = ""
        if self.props:
            for key, value in self.props.items():
                attrs_str += f' {key}="{value}"'
        return f"<{self.tag}{attrs_str}>{self.value}</{self.tag}>"