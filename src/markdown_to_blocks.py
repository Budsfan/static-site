from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(string):
    block_list = []
    for block in string.split("\n\n"):
        if len(block) == 0:
            continue
        block_list.append(block.strip())
    return block_list

def block_to_block_type(block):
    if not isinstance(block, str):
        raise TypeError('Can only process text blocks')
    elif block[0] == "#":
        return BlockType.HEADING
    elif block[0:3] == "```" and block[len(block)-3:len(block)] == "```":
        return BlockType.CODE
    elif block[0] == ">" and len(block) > 1:
        return BlockType.QUOTE
    elif block[0] == "-" and len(block) > 1:
        return BlockType.UNORDERED_LIST
    elif block[0].isdigit() and block[1] == ".":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH




    

