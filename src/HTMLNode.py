

class HTMLNODE():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is not None:
            parts = [f' {k}="{v}"' for k, v in self.props.items()]
            return "".join(parts)
        return ''
    def __repr__(self):
        return f"HTMLNode:{self.tag}, {self.value}, Children: {self.children}, {self.props}"
    
class LeafNode(HTMLNODE):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"Leaf Node:{self.tag}, {self.value}, {self.props}"
    
class ParentNode(HTMLNODE):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, children=children, props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError('tag is None')
        if self.children is None:
            raise ValueError('children is None')
        return_str = ''
        for child in self.children:
            return_str += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{return_str}</{self.tag}>"