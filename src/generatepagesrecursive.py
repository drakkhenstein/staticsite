import os
from generatepage import generate_page
import shutil
import sys

def generate_pages_recursive(dir_path, template_path, dest_dir_path, basepath):
    # Create the output directory
    os.makedirs(dest_dir_path, exist_ok=True)
    
    # Get all items in the directory
    items = os.listdir(dir_path)
    
    # Loop through all items
    for item in items:
        # Create the full paths
        source_path = os.path.join(dir_path, item)
        dest_path = os.path.join(dest_dir_path, item)
        
        # Check if the item is a file
        if os.path.isfile(source_path):
            # If it's a markdown file, generate an HTML page
            if source_path.endswith(".md"):
                print(f"Generating page: {source_path} to {dest_path.replace('.md', '.html')}")
                generate_page(source_path, template_path, dest_path.replace(".md", ".html"), basepath)
            
        else:
            # If it's a directory, recursively generate pages in that directory
            print(f"Processing directory: {source_path} to {dest_path}")
            os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(source_path, template_path, dest_path, basepath)