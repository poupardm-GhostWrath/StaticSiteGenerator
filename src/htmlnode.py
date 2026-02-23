from textnode import *
from splitnode import *
from extract_markdown import *


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        output = ""
        if self.props is None or len(self.props) == 0:
            return output
        for item in self.props:
            output += f' {item}="{self.props[item]}"'
        return output
    
    def __repr__(self):
        return f'tag="{self.tag}" value="{self.value}" children="{self.children}" props="{self.props}"'
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("Error: value is None")
        if self.tag is None:
            return self.value
        else:
            if self.props is not None:
                match self.tag:
                    case "a":
                        return f'<a href="{self.props["href"]}">{self.value}</a>'
                    case "img":
                        return f'<img src="{self.props["src"]}" alt="{self.value}" />'
            else:
                return f"<{self.tag}>{self.value}</{self.tag}>"
            
    def __repr__(self):
        return f'tag="{self.tag}" value="{self.value}" props="{self.props}"'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Error: tag is missing")
        if self.children is None:
            raise ValueError("Error: children are missing")
        output = f"<{self.tag}>"
        for child in self.children:
            output += child.to_html()
        output += f"</{self.tag}>"
        return output
    
def text_node_to_html_node(text_node):
    if text_node is None:
        raise Exception("Error: Node is NoneType")
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", text_node.text, {"src":text_node.url})
        case _:
            raise Exception("Error: Invalid Text Type")
        
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    # Split images out
    nodes = split_nodes_image(nodes)
    # Split links out
    nodes = split_nodes_link(nodes)
    # Split bold out
    nodes = split_nodes_bold(nodes)
    # Split italic out
    nodes = split_nodes_italic(nodes)
    # Split code out
    nodes = split_nodes_code(nodes)
    return nodes

                