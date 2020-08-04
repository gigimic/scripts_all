import pyinputplus as pyip

# print(pyinputplus.__version__)

# inputStr() Is like the built-in input() function but has the general PyInputPlus features. 
# You can also pass a custom validation function to it

# inputNum() Ensures the user enters a number and returns an int or float, 
# depending on if the number has a decimal point in it

# inputChoice() Ensures the user enters one of the provided choices

# inputMenu() Is similar to inputChoice(), but provides a menu with numbered or lettered options

# inputDatetime() Ensures the user enters a date and time

# inputYesNo() Ensures the user enters a “yes” or “no” response

# inputBool() Is similar to inputYesNo(), but takes a “True” or “False” response and 
# returns a Boolean value

# inputEmail() Ensures the user enters a valid email address

# inputFilepath() Ensures the user enters a valid file path and filename, and 
# can optionally check that a file with that name exists

# inputPassword() Is like the built-in input(), but displays * characters as 
# the user types so that passwords, or other sensitive information, aren’t displayed on the screen

# These functions will automatically reprompt the user for as long as they enter invalid input:

# The inputNum(), inputInt(), and inputFloat() functions, which accept int and float numbers, 
# also have min, max, greaterThan, and lessThan keyword arguments for specifying 
# a range of valid values.

response = pyip.inputNum('Enter your age:   ', min = 1, max = 120)
print('Your age is  :',  response)

# Here blank is an option
response = pyip.inputNum('Enter a number :  ', blank=True)

# This input wont accept even numbers 
response = pyip.inputNum(blockRegexes=[r'[02468]$'])
 
# Here the input accepts only yes or no  
prompt = 'Want to go to London?\n'
response = pyip.inputYesNo(prompt)
if response == 'no':
    print('so sad')
else:
    print('lets go')

print('Thank you. Have a nice day.')