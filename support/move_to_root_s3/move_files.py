import os
import shutil

root_dir = "/Users/bisshwajitsamanta/temp/archived_contents"

dir_list = []

for dir in os.listdir(root_dir):
    d = os.path.join(root_dir,dir)
    if os.path.isdir(d):
        dir_list.append(d)

for el in dir_list:
    # List all Files
    all_files = os.listdir(el)

    for files in all_files:
        src_path = os.path.join(el,files)
        dst_path = os.path.join(root_dir,files)
        shutil.move(src_path,dst_path)