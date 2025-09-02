# rename_files.py
import os

folder_path = r'C:\Users\Herob\Documents\test_folder'
prefix = 'new_'

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        old_path = os.path.join(folder_path, filename)
        new_filename = prefix + filename
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f'Renamed: {filename} -> {new_filename}')