import subprocess
import os
import psutil

tmp_dir = os.path.join('/', 'tmp')
# tmp_dir = '/root/Desktop/fff/'
print(tmp_dir)

def lsof(path=None):
    users = []
    for p in psutil.process_iter():
        files = []
        try:
            files = p.open_files()
        except:
            pass
        if path:
            users.extend([(f.path, p.name(), p.pid, p.username()) for f in files if f.path in path])
        else:
            users.extend([(f.path, p.name(), p.pid, p.username()) for f in files])
    return users


for root, dirs, files in os.walk(tmp_dir):
    count = 0
    # print(dirs)
    if len(files) != 0:
        for file in files:
            path_ = os.path.join(root, file)
            # print(path_)
            li = lsof(path_)
            if len(li) == 0:
                # print(path_)
                count += 1
                subprocess.run(["rm", '-f', path_])
        if count == len(files):
            subprocess.run(["rm", '-rf', root])
    else:
        for dir in dirs:
            if len(lsof(dir)) == 0:
                subprocess.run(["rm", '-rf', dir])
