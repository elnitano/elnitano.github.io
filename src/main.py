import os
import shutil
import sys
from generate_page import generate_pages_recursive

def copy_files(static, public):
    if not os.path.exists(public):
        os.mkdir(public)
    
    for filename in os.listdir(static):
        source_path = os.path.join(static, filename)
        dest_path = os.path.join(public, filename)
        print(f"Copying {source_path} => {dest_path}")
        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            copy_files(source_path, dest_path)


dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():
    # Checks for system argument, for basepath
    # Example: "main.py /ht_docs/"
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    # Checks if public folder exist, and removes if does.
    print(f"Deleting public folder: {dir_path_public}")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    # Copy Static folder to Public Folder (Recursively because we love that!)
    print(f"Copying files from {dir_path_static} to {dir_path_public}")
    copy_files(dir_path_static, dir_path_public)

    # Generate the content
    print("Generating HTML content")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

main()