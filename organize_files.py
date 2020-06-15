import shutil, os
shutil.copy('data1.csv', 'data11.csv')
# Here full path name can be given to copy files

shutil.move('/path/from/file1', 'path/to') #moving files
shutil.move('/path/from/file1', 'path/to/file2') # renaming files