import os
import shutil

from_dir="C:/Users/52563/Downloads"
to_dir="C:/Users/52563/Desktop/Documentos_Archivos"
list_off_files=os.listdir(from_dir)
print(list_off_files)
for file_name in list_off_files:
    name,extension=os.path.splitext(file_name)
    print(name)
    print(extension)