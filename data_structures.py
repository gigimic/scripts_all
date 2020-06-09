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