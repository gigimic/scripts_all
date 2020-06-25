import shutil, os, re
# Renaming Files with American-Style Dates to European-Style Dates
# 1.Create a regex that can identify the text pattern of American-style dates.
# 2.Call os.listdir() to find all the files in the working directory.
# 3.Loop over each filename, using the regex to check whether it has a date.
# 4.If it has a date, rename the file with shutil.move().

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
((0|1)?\d)-                     # one or two digits for the month
((0|1|2|3)?\d)-                 # one or two digits for the day
((19|20)\d\d)                   # four digits for the year
(.*?)$                          # all text after the date
""", re.VERBOSE)

# Here re.VERBOSE is used so that the comments can be written in between 

# print(datePattern)

# following is a test code to find all the csv files using pattern search 
patt = re.compile('csv')
for file in os.listdir('.'):
    mo = patt.search(file)
    if mo is not None:
        print(file)


# TODO: Loop over the files in the working directory.

# TODO: Skip files without a date.

# TODO: Get the different parts of the filename.

# TODO: Form the European-style filename.

# TODO: Get the full, absolute file paths.

# TODO: Rename the files.