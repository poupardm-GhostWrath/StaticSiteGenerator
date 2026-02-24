import os
import shutil

def copy_folder_content(source, target):
    # Check if source exist
    if os.path.exists(source) == False:
        raise Exception("Invalid source")

    # Get Absolute Path for source
    source_abs = os.path.abspath(source)

    # Create target folder if doesn't exist
    if os.path.exists(target) == False:
        os.mkdir(target)
    
    # Get Absolute Path for target
    target_abs = os.path.abspath(target)

    # Check if target is not empty
    if len(os.listdir(target_abs)) > 0:
        # Delete entire target folder
        shutil.rmtree(target_abs)
        # Re-create target folder
        os.mkdir(target_abs)

    # Get Content of Source Directory
    source_content = os.listdir(source_abs)
    for item in source_content:
        # Check is item isfile
        if os.path.isfile(os.path.join(source_abs, item)):
            # Copy file to target folder
            shutil.copy(os.path.join(source_abs, item), target_abs)
        else:
            # Copy folder content to target folder
            copy_folder_content(os.path.join(source_abs, item), os.path.join(target_abs, item))
        
    
    
    

def main():
    copy_folder_content("static", "public")
    pass

if __name__ == "__main__":
    main()