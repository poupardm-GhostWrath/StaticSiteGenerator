from block_markdown import markdown_to_html_node, extract_title
from htmlnode import *
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Open and read from_path file
    md_file = open(from_path)
    md = md_file.read()
    md_file.close()

    # Open and read template_path file
    template_file = open(template_path)
    template_data = template_file.read()
    template_file.close()

    # Convert markdown to html string
    html_node = markdown_to_html_node(md)
    html_string = html_node.to_html()

    # Extract title from markdown
    title = extract_title(md)

    # Replace placeholders
    new_html = template_data.replace("{{ Title }}", title)
    new_html = new_html.replace("{{ Content }}", html_string)

    # Get dir for file
    dir_name = os.path.dirname(dest_path)
    os.makedirs(dir_name, exist_ok=True)
    dest_file = open(dest_path, mode="w")
    amount_wrote = dest_file.write(new_html)
    dest_file.close()