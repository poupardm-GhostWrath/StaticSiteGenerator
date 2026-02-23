from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    document = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block == "":
            continue
        document.append(block.strip())
    return document

def block_to_block_type(text):
    if len(re.findall(r"\#{1,6} (.*)", text)) == 1:
        return BlockType.HEADING
    if len(re.findall(r"\`{3}\n(^[\s\S]+$)\n\`{3}", text, re.MULTILINE)) == 1:
        return BlockType.CODE
    if len(re.findall(r"\> {0,1}(.*)", text)) == 1:
        return BlockType.QUOTE
    if len(re.findall(r"\- (.*)", text)) == 1:
        return BlockType.UNORDERED_LIST
    if len(re.findall(r"\d{1,}. (.*)", text)) == 1:
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH