import os
from pygwy_txt_analysis import get_folder_path
import glob
import shutil

import_folder = get_folder_path()
export_folder = get_folder_path()

name_string = "rs67_10mg-ml_period-sweep"

for folder in glob.glob(os.path.join(import_folder, '*')):
    filepath = os.path.join(folder, 'export/stat_plots/*.csv')
    x_value = os.path.basename(folder)
    for file in glob.glob(filepath):
        if os.path.basename(file) == 'data_height_plot.csv':
            new_file_name = name_string + f'_{x_value}_height.csv'
        else:
            new_file_name = name_string + f'_{x_value}_period.csv'

        dst = os.path.join(export_folder, new_file_name)
        shutil.copy2(file, dst)
