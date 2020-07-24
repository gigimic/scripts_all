import re

# following are the functions and descriptions.

# findall  :	Returns a list containing all matches
# search	 :  Returns a Match object if there is a match anywhere in the string
# split	 :   Returns a list where the string has been split at each match
# sub	     :   Replaces one or many matches with a string



# finding a pattern from a string

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' +  mo.group())

# finding a pattern from a string as different groups

phoneNumRegex = re.compile(r'(\d{3})-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('first part ',  mo.group(1))

# finding a pattern from a string with repeated characters and optional entries
phoneNumRegex = re.compile(r'(\d{3})(-)?(\d{3}-\d{4})')
mo = phoneNumRegex.search('My number is 415555-4242.')
print('number   ',  mo.group(1))

# Matching Newlines with the Dot Character

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# Case-Insensitive Matching
# To make your regex case-insensitive, 
# you can pass re.IGNORECASE or re.I as 
# a second argument to re.compile(). 

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())

print(robocop.search('ROBOCOP protects the innocent.').group())

print(robocop.search('Al, why does your programming book talk about robocop so much?').group())


# character classes 
# \d  Any numeric digit from 0 to 9.
# \D Any character that is not a numeric digit from 0 to 9.
# \w  Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W  Any character that is not a letter, numeric digit, or the underscore character.
# \s  Any space, tab, or newline character. (Think of this as matching “space” characters.)
# \S  Any character that is not a space, tab, or newline.


# In the following example the regular expression \d+\s\w+ will match text that has 
# one or more numeric digits (\d+), followed by a whitespace character (\s), 
# followed by one or more letter/digit/underscore characters (\w+). 
# The findall() method returns all matching strings of the regex pattern in a list.


xmasRegex = re.compile(r'\d+\s\w+')
print(xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 2 doves'))

# character class can be defined in square brackets
robocop = re.compile('[robocop]') #each character is searched in thw string
print(robocop.findall('RoboCop is part man, part machine, all cop.'))
robo = re.compile('[^a-zA-Z]')
print(robo.sub(' ', 'RoboCop is part man, part machine, all cop.').lower())