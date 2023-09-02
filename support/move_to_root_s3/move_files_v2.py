import os
import shutil

root_dir = "/Users/bisshwajitsamanta/temp/archived_contents"
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        src_path = os.path.join(dirpath, filename)
        dst_path = os.path.join(root_dir, filename)
        shutil.move(src_path, dst_path)

for dirpath, dirnames, filenames in os.walk(root_dir,topdown=False):
    print(f'Directory Names: {dirnames}')
    for dir in dirnames:
        print(f'Individual Names: {dir}')
        print(f'Directory Path: {dirpath}')
        full_path = os.path.join(dirpath,dir)
        print(f'Full Path: {full_path}')
        if not os.listdir(full_path):
            os.rmdir(full_path)