import os
import shutil

folder = 'templates'
if not os.path.exists(folder):
    os.mkdir(folder)

direct = r'my_project'
files = []

for r, d, f in os.walk(direct):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(folder, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)