from textnode import TextType, TextNode
import os
import shutil
from markdown_to_html_node import markdown_to_html_node
from HTMLNode import HTMLNODE

def copy_dir(origin, destination):
    if not os.path.exists(origin):
        raise Exception(f"Path: {origin} does not exist")
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    for item in os.listdir(origin):
        full_origin_path = os.path.join(origin, item)
        full_destination_path = os.path.join(destination, item)
        if os.path.isfile(full_origin_path):
            shutil.copy(full_origin_path, full_destination_path)
        elif os.path.isdir(full_origin_path):
            copy_dir(full_origin_path, full_destination_path)

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if len(line) > 0:
            if line[0] == "#" and line[1] != "#":
                return line.split("#", maxsplit=1)[1].strip()
            
    raise ValueError('Markdown must contain h1 title')

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    if os.path.isfile(from_path):
        with open(from_path, "r") as from_file:
            with open(template_path, "r") as template_file:
                from_contents = from_file.read()
                template_contents = template_file.read()
                node = markdown_to_html_node(from_contents)
                html = node.to_html()
                title = extract_title(from_contents)
                template_contents = template_contents.replace("{{ Title }}", title)
                template_contents = template_contents.replace("{{ Content }}", html)
        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
        if dest_path[-3:] == ".md":
            dest_path = dest_path[:-3] + ".html"
        with open(dest_path, "w") as f:
            f.write(template_contents)

def page_generator(root, template_path, dest_path):
    for item in os.listdir(root):
        current = os.path.join(root, item)
        if item[-3:] == ".md":
            generate_page(current, template_path, os.path.join(dest_path, item))
        elif os.path.isdir(current):
            page_generator(os.path.join(root, item), template_path, os.path.join(dest_path, item))

def main():
    copy_dir("static", "public")
    page_generator("content", "template.html", "public")
main()