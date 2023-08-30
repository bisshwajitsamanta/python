import os
import shutil

root_dir = "/Users/bisshwajitsamanta/temp/archived_contents"
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        src_path = os.path.join(dirpath, filename)
        dst_path = os.path.join(root_dir, filename)
        shutil.move(src_path, dst_path)

for dirpath, dirnames, filenames in os.walk(root_dir,topdown=False):
    for dir in dirnames:
        full_path = os.path.join(dirpath,dir)
        if not os.listdir(full_path):
            os.rmdir(full_path)