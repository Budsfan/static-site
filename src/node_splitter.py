from textnode import TextType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    lst = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            lst.append(node)
        else:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise Exception('delimiter not closed')
            for i in range(0, len(parts)):
                if parts[i] == "":
                    continue
                if i % 2 == 0:
                    lst.append(TextNode(parts[i], TextType.TEXT))
                else:
                    lst.append(TextNode(parts[i], text_type))
    return lst

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
def split_nodes_image(old_nodes):
    lst = []
    for node in old_nodes:
        text = node.text
        extracted_images = extract_markdown_images(node.text)
        if len(extracted_images) == 0:
            lst.append(node)
            continue
        for image in extracted_images:
            parts = text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
            if len(parts[0]) > 0:
                new_node = TextNode(parts[0], TextType.TEXT)
                lst.append(new_node)
            lst.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text = parts[1]
        if len(parts[1]) > 0:
            new_node = TextNode(parts[1], TextType.TEXT)
            lst.append(new_node)
    return lst

def split_nodes_link(old_nodes):
    lst = []
    for node in old_nodes:
        text = node.text
        extracted_links = extract_markdown_links(node.text)
        if len(extracted_links) == 0:
            lst.append(node)
            continue
        for link in extracted_links:
            parts = text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
            if len(parts[0]) > 0:
                new_node = TextNode(parts[0], TextType.TEXT)
                lst.append(new_node)
            lst.append(TextNode(link[0], TextType.LINK, link[1]))
            text = parts[1]
        if len(parts[1]) > 0:
            new_node = TextNode(parts[1], TextType.TEXT)
            lst.append(new_node)
    return lst

def text_to_textnodes(text):
    text = split_nodes_delimiter(text, "**", TextType.BOLD_TEXT)
    text = split_nodes_delimiter(text, "_", TextType.ITALIC_TEXT)
    text = split_nodes_delimiter(text, '`', TextType.CODE_TEXT)
    text = split_nodes_image(text)
    text = split_nodes_link(text)
    return text





