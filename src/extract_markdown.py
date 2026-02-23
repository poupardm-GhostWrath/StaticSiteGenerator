import re

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def extract_markdown_bold(text):
    return re.findall(r"\*\*(.*?)\*\*", text)

def extract_markdown_italic(text):
    return re.findall(r"\_(.*?)\_", text)

def extract_markdown_code(text):
    return re.findall(r"\`(.*?)\`", text)