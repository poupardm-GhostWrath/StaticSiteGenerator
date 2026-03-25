from block_markdown import markdown_to_html_node
import os
from pathlib import Path

def generate_page(basepath, from_path, template_path, dest_path):
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
    new_html = new_html.replace('href="/', f'href="{basepath}')
    new_html = new_html.replace('src="/', f'src="{basepath}')

    # Get dir for file
    dir_name = os.path.dirname(dest_path)
    if dir_name != "":
        os.makedirs(dir_name, exist_ok=True)
    dest_file = open(dest_path, mode="w")
    amount_wrote = dest_file.write(new_html)
    dest_file.close()

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")

def generate_page_recursive(basepath, dir_path_content, template_path, dest_dir_path):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(basepath, from_path, template_path, dest_path)
        else:
            generate_page_recursive(basepath, from_path, template_path, dest_path)