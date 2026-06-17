from pygwy_txt_analysis import get_folder_path
import glob
import os
import shutil


basepath = get_folder_path()
folder_list = glob.glob(os.path.join(basepath, '*'))

file_list = glob.glob(os.path.join(folder_list[0], '*.txt'))

for file in file_list:
    filename = os.path.basename(file)[:-4]
    os.makedirs(os.path.join(basepath, filename), exist_ok=True)

for folder in folder_list:
    for file in glob.glob(os.path.join(folder, '*.txt')):
        dst = os.path.join(basepath, os.path.basename(file)[:-4], os.path.basename(folder)+'.txt')
        shutil.copy2(file, dst)