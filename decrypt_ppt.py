import sys
import os
import pathlib
import shutil
from zipfile import ZipFile
import subprocess
import re
file1 = sys.argv
encr_file = file1[1]
new_file_inter = str(pathlib.Path(encr_file).stem) 
new_file = new_file_inter + ".zip"
new_file_copy = new_file_inter + "_cp.zip"
os.rename(encr_file,new_file)
shutil.copy(new_file,new_file_copy)
archive = ZipFile(new_file_copy)
for file in archive.namelist():
    if file.startswith('ppt/'):
        archive.extract(file)
file_to_change = "ppt/presentation.xml"
file1 = open(file_to_change, "r")
s =file1.read()
file1.close()
new_s = re.sub(r"<p:modifyVerifier[^>]+>", '',s)
file1 = open(file_to_change, "w+")
file1.write(new_s)
file1.close()
subprocess.call(["zip", "-r", new_file, file_to_change])
os.rename(new_file, encr_file)
os.remove(new_file_copy)
folder_to_remove = str(pathlib.Path(file_to_change).parent)
shutil.rmtree(folder_to_remove)
