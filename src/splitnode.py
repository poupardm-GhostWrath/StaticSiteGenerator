from textnode import *
from extract_markdown import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            if delimiter not in node.text:
                raise Exception("Error: Invalid Markdown Syntax")
            else:
                split_node = node.text.split(delimiter)
                if len(split_node) < 3:
                    raise Exception("Error: Invalid Markdown syntax")
                for i in range(len(split_node)):
                    if i % 2 != 0:
                        new_nodes.append(TextNode(split_node[i], text_type))
                    else:
                        new_nodes.append(TextNode(split_node[i], TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            delimiters = extract_markdown_images(node.text)
            remainder = node.text
            for i in range(0, len(delimiters)):
                image_alt = delimiters[i][0]
                image_link = delimiters[i][1]
                split_node = remainder.split(f"![{image_alt}]({image_link})", 1)
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                remainder = split_node[1]
            if remainder != "":
                new_nodes.append(TextNode(remainder, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            delimiters = extract_markdown_links(node.text)
            remainder = node.text
            for i in range(0, len(delimiters)):
                link_text = delimiters[i][0]
                link_url = delimiters[i][1]
                split_node = remainder.split(f"[{link_text}]({link_url})", 1)
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
                remainder = split_node[1]
            if remainder != "":
                new_nodes.append(TextNode(remainder, TextType.TEXT))
    return new_nodes

def split_nodes_bold(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            delimiters = extract_markdown_bold(node.text)
            remainder = node.text
            for i in range(0, len(delimiters)):
                text = delimiters[i]
                split_node = remainder.split(f"**{text}**", 1)
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(text, TextType.BOLD))
                remainder = split_node[1]
            if remainder != "":
                new_nodes.append(TextNode(remainder, TextType.TEXT))
    return new_nodes

def split_nodes_italic(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            delimiters = extract_markdown_italic(node.text)
            remainder = node.text
            for i in range(0, len(delimiters)):
                text = delimiters[i]
                split_node = remainder.split(f"_{text}_", 1)
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(text, TextType.ITALIC))
                remainder = split_node[1]
            if remainder != "":
                new_nodes.append(TextNode(remainder, TextType.TEXT))
    return new_nodes

def split_nodes_code(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            delimiters = extract_markdown_code(node.text)
            remainder = node.text
            for i in range(0, len(delimiters)):
                text = delimiters[i]
                split_node = remainder.split(f"`{text}`", 1)
                new_nodes.append(TextNode(split_node[0], TextType.TEXT))
                new_nodes.append(TextNode(text, TextType.CODE))
                remainder = split_node[1]
            if remainder != "":
                new_nodes.append(TextNode(remainder, TextType.TEXT))
    return new_nodes