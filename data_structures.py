# dictionaries are unordered while lists are ordered 

animals1 = ['cats', 'dogs', 'moose']
animals2 = ['dogs', 'moose', 'cats']
print(animals1 == animals2)
# The answer is False as it compares index by index

names1 = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
names2 = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(names1 == names2)
# The answer is True as the dictionary is unordered

print(names1['color'])
# This gives a keyError just like out-of-range index errror message