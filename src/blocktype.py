from enum import Enum
from leafnode import LeafNode
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def is_heading(block):
    return bool(re.match(r'^#{1,6} ', block))

def block_to_block_type(block):
    if is_heading(block):
        return BlockType.HEADING
    if block.startswith('```') and block.endswith('```'):
        return BlockType.CODE
    
    lines = block.split('\n')
    
    if all(line.startswith('>') for line in lines):
        return BlockType.QUOTE
    if all(line.startswith('- ') for line in lines):
        return BlockType.UNORDERED_LIST

    ordered_list = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i + 1}. "
        if not line.startswith(expected_prefix):
            ordered_list = False
            break
    if ordered_list:
        return BlockType.ORDERED_LIST
   
    return BlockType.PARAGRAPH

