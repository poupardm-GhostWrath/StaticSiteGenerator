import os
import shutil
from page_generator import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"

def copy_folder_content(source, target):
    # Create target folder if doesn't exist
    if os.path.exists(target) == False:
        os.mkdir(target)

    # Get Content of Source Directory
    for item in os.listdir(source):
        from_path = os.path.join(source, item)
        dest_path = os.path.join(target, item)
        print(f" * {from_path} -> {dest_path}")
        # Check is item isfile
        if os.path.isfile(from_path):
            # Copy file to target folder
            shutil.copy(from_path, dest_path)
        else:
            # Copy folder content to target folder
            copy_folder_content(from_path, dest_path)

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_folder_content(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_page_recursive(
        dir_path_content, 
        template_path, 
        dir_path_public
    )


if __name__ == "__main__":
    main()