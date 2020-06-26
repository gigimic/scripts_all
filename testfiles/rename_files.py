import shutil, os, re

# Here all the files in the directory with a space is renamed with the space removed
# Only the last two lines are required for this purpose

for file in os.listdir('.'):
    file_parts = file.split(' ')
    print(file, file_parts)
    mod_file = ''.join(file_parts)
    print(file, mod_file)
    shutil.move(file, mod_file)
    

for file in os.listdir('.'):
    print(file)


words = 'dogs and cats'
words_together = ''.join(words.split(' '))
print(words, words_together)

# The following two lines replaces the lines 5-10 of the code

for file in os.listdir('.'):
    shutil.move(file, ''.join(file.split(' ')))

# Project: Backing Up a Folder into a ZIP File
# Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    folder = os.path.abspath(folder)   # make sure folder is absolute

       # Figure out the filename this code should use based on
       # what files already exist.
    number = 1
    while True:
           zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
           if not os.path.exists(zipFilename):
               break
           number = number + 1

    # TODO: Create the ZIP file.

       # TODO: Walk the entire folder tree and compress the files in each folder.
       print('Done.')

backupToZip('folder')