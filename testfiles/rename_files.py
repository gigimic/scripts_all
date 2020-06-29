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

    #  Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')


    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
     backupZip.close()
    
    print('Done.')

backupToZip('folder') # folder is the folder, the contents of which are to be backed up

