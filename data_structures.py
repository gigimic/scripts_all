# dictionaries are unordered while lists are ordered 

animals1 = ['cats', 'dogs', 'moose']
animals2 = ['dogs', 'moose', 'cats']
print(animals1 == animals2)
# The answer is False as it compares index by index

names1 = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
names2 = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(names1 == names2)
# The answer is True as the dictionary is unordered

# print(names1['color'])
# This gives a keyError just like out-of-range index errror message

# dictionaried are powerful though not ordered 
# Here we can get information from an existing dictionaries and append information 
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break

#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')

print(birthdays)

# keys(), values(), and items() can be accessed in different ways

for ones in birthdays.values():
    print(ones)

for ones in birthdays.keys():
    print(ones)

for ones in birthdays.items():
    print(ones)

for k, v in birthdays.items():
    print('Key: ' + k + ' Value: ' + str(v))
print('#######')
print(list(birthdays.keys()))

# Checking Whether a Key or Value Exists in a Dictionary
print('Bob' in birthdays.keys())  #returns TRUE
print('Kevin' in birthdays.keys()) #returns False

# The get() Method dictionaries have a get() method that takes two arguments: 
# the key of the value to retrieve and a fallback value to return if that key does not exist

print('This birthday ' + str(birthdays.get('Bob', 0)) + '  belongs to '+ 'Bob.')

# The setdefault() Method

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black') #wherever the key 'color' doesnt exist, this statement provides one

print(list(spam.items()))

# The setdefault() method is a nice shortcut to ensure that a key exists. 
# This program counts the number of occurrences of each letter in a string.

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
# If you import the pprint module into your programs, you’ll have access to 
# the pprint() and pformat() functions that will “pretty print” a dictionary’s values. 

import pprint 
pprint.pprint(count)


