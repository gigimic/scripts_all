import shutil, os
shutil.copy('data1.csv', 'data11.csv')
# Here full path name can be given to copy files

shutil.move('/path/from/file1', 'path/to') #moving files
shutil.move('/path/from/file1', 'path/to/file2') # renaming files

# Permanently Deleting Files and Folders

from pathlib import Path
home_folder=Path.home()
reguired_folder = home_folder/'trial'
for filename in reguired_folder.glob('*.txt'):
    #os.unlink(filename)
    print(filename)

# os.unlink(filename) deletes the filename
# os.rmdir(folder) deletes the folder if the folder is empty
# shutil.rmtree(folder) will remove the folder and all files and folders it contains.

# Safe Deletes with the send2trash Module

import send2trash
send2trash.send2trash('filename') # sends the file to trash

 

# Walking a Directory Tree

for folder_name, subfolders, filenames in os.walk(reguired_folder/'testfiles'):
    print('The current folder is ' + folder_name)

    for subfolder in subfolders:
        print('SUBFOLDER OF ' + folder_name + ': ' + subfolder)

    for filename in filenames:
        print('FILE INSIDE ' + folder_name + ': '+ filename)

    print('')


# Compressing Files with the zipfile Module

import zipfile
# reading contents of a zipfile 

exampleZip = zipfile.ZipFile('example.zip')
exampleZip.namelist() #provides the names of the files in the zip
fileInfo = exampleZip.getinfo('filename')
print(fileInfo.file_size) # provides the file size
fileInfo.compress_size
exampleZip.close()