from textnode import TextNode, TextType
from generatepage import generate_page
from generatepagesrecursive import generate_pages_recursive
import os
import shutil
import sys

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

def copy_static_files(source_dir, dest_dir):
    # First, check if the destination directory exists and delete it if it does
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    
    # Create the destination directory
    os.mkdir(dest_dir)
    
    # Get all items in the source directory
    items = os.listdir(source_dir)
    
    # Loop through all items
    for item in items:
        # Create the full paths
        source_path = os.path.join(source_dir, item)
        dest_path = os.path.join(dest_dir, item)
        
        # Check if the item is a file
        if os.path.isfile(source_path):
            # If it's a file, copy it
            print(f"Copying file: {source_path} to {dest_path}")
            shutil.copy(source_path, dest_path)
        else:
            # If it's a directory, recursively copy it
            print(f"Copying directory: {source_path} to {dest_path}")
            os.mkdir(dest_path)
            copy_static_files(source_path, dest_path)


def main():
    content_dir = "content"
    template_path = "template.html"
    public_dir = "docs"
    copy_static_files("static", "docs")
    #print("About to generate page")
    generate_pages_recursive(content_dir, template_path, public_dir, basepath)
    #print("Page generated")
    
if __name__ == "__main__":
    main()