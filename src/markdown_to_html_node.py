from markdown_to_blocks import markdown_to_blocks, block_to_block_type, BlockType
from HTMLNode import HTMLNODE, LeafNode, ParentNode
from node_splitter import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType



def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            block_nodes.append(code_parent_block(block))
        elif block_type == BlockType.HEADING:
            block_nodes.append(heading_parent_block(block))
        elif block_type == BlockType.ORDERED_LIST:
            block_nodes.append(ordered_list_parent_block(block))
        elif block_type == BlockType.PARAGRAPH:
            block_nodes.append(paragraph_parent_block(block))
        elif block_type == BlockType.QUOTE:
            block_nodes.append(quote_parent_block(block))
        elif block_type == BlockType.UNORDERED_LIST:
            block_nodes.append(unordered_list_parent_block(block))
    return ParentNode("div", block_nodes)

def text_to_children(text):
    text_nodes = text_to_textnodes([TextNode(text, TextType.TEXT)])
    children = []
    for node in text_nodes:
        children.append(text_node_to_html_node(node))
    return children

def code_parent_block(text):
    child_text_node = TextNode(text[4:-3], TextType.TEXT)
    child_html = text_node_to_html_node(child_text_node)
    inner_tag = ParentNode("code", [child_html])
    outter_tag = ParentNode("pre", [inner_tag])
    return outter_tag

def heading_parent_block(text):
    level = len(text) - len(text.lstrip("#"))
    value = text[level:].strip()
    parent_tag = f"h{level}"
    return ParentNode(parent_tag, text_to_children(value))
    
def ordered_list_parent_block(text):
    children = []
    for line in text.splitlines():
        item_text = line.split(".", maxsplit=1)[1].strip()
        children.append(ParentNode("li", text_to_children(item_text)))
    return ParentNode("ol", children)

def paragraph_parent_block(text):
    return ParentNode("p", text_to_children(" ".join(text.splitlines())))

def quote_parent_block(text):
    return ParentNode("blockquote", text_to_children(text))

def unordered_list_parent_block(text):
    children = []
    for line in text.splitlines():
        item_text = line.split("-", maxsplit=1)[1].strip()
        children.append(ParentNode("li", text_to_children(item_text)))
    return ParentNode("ul", children)
    
