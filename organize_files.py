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

exampleZip.extractall() 
#  The extractall() method for ZipFile objects extracts all the files and folders 
#  from a ZIP file into the current working directory.
exampleZip.extractall('folder name') #contnts will be extracted to the given folder
exampleZip.extract('filename to be extracted', 'target folder name') 
exampleZip.close()

# creating and adding to zipfiles 
import zipfile
# open the zipfile to be created in write mode 
newZip = zipfile.ZipFile('new.zip', 'w')
# compression type parameter, which tells the computer 
# what algorithm it should use to compress the files
# the compression type zipfile.ZIP_DEFLATED specifies 
# the deflate compression algorithm, which works well on all types of data
newZip.write('spam.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

# Renaming Files with American-Style Dates to European-Style Dates
# 1.Create a regex that can identify the text pattern of American-style dates.
# 2.Call os.listdir() to find all the files in the working directory.
# 3.Loop over each filename, using the regex to check whether it has a date.
# 4.If it has a date, rename the file with shutil.move().

import shutil, os, re

   # Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1)?\d)-                     # one or two digits for the month
((0|1|2|3)?\d)-                 # one or two digits for the day
((19|20)\d\d)                   # four digits for the year
(.*?)$                          # all text after the date
""", re.VERBOSE➌)

# TODO: Loop over the files in the working directory.

# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.