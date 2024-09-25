import os

folder = r"C:\Users\TetsaPD\Desktop\ewwbsite\media"

for file in os.listdir(folder):
    old_file_path = os.path.join(folder, file)
    if os.path.isfile(old_file_path):
        new_filename = file.replace(".jpg_", "") + ''
        new_file_path = os.path.join(folder, new_filename)
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {file} -> {new_filename}')
