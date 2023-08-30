import os
import shutil
from time import perf_counter
from datetime import datetime

root_dir = "/Users/bisshwajitsamanta/temp/archived_contents"
print(f'{datetime.utcnow().isoformat()} - Starting of the script')
start = perf_counter()
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
end = perf_counter()
print(f'{datetime.utcnow().isoformat()} - Re-organising Script Successfully completed in :: {end - start}')