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
