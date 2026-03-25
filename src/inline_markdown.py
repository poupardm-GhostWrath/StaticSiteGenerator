import re
from textnode import TextNode, TextType

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        split_nodes = []
        split_node = node.text.split(delimiter)
        if len(split_node) % 2 == 0:
            raise Exception("Error: Invalid Markdown syntax")
        for i in range(len(split_node)):
            if split_node[i] == "":
                continue
            if i % 2 != 0:
                split_nodes.append(TextNode(split_node[i], text_type))
            else:
                split_nodes.append(TextNode(split_node[i], TextType.TEXT))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        delimiters = extract_markdown_images(node.text)
        remainder = node.text
        if len(delimiters) == 0:
            new_nodes.append(node)
            continue 
        for delimiter in delimiters:
            split_node = remainder.split(f"![{delimiter[0]}]({delimiter[1]})", 1)
            if len(split_node) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(delimiter[0], TextType.IMAGE, delimiter[1]))
            remainder = split_node[1]
        if remainder != "":
            new_nodes.append(TextNode(remainder, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
            continue
        delimiters = extract_markdown_links(node.text)
        remainder = node.text
        if len(delimiters) == 0:
            new_nodes.append(node)
            continue
        for delimiter in delimiters:
            split_node = remainder.split(f"[{delimiter[0]}]({delimiter[1]})", 1)
            if len(split_node) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if split_node[0] != "":
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
            new_nodes.append(TextNode(delimiter[0], TextType.LINK, delimiter[1]))
            remainder = split_node[1]
        if remainder != "":
            new_nodes.append(TextNode(remainder, TextType.TEXT))
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)