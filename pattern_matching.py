import re

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