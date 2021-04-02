# a few tricks in python to make life easier

# 1. use enumerate in loops to get index and list items
items=['a', 'b', 'c']
for index, item in enumerate(items):
    print(index, item)
    
# 2. .get() to get dictionary items 
person ={"name": 'Rachel',
        "age" : 32,
        "gender": 'Female'}

print(person['name'], '\t', person['age'])
# print(person['name'], '\t', person['location']) # gives an error as 'location' is not defined
print(person['name'], '\t', person.get('location')) # gives 'None' and not program error 

# 3. using zip
names = ['Nik', 'Jane', 'Melissa', 'Doug']
ages = [32, 28, 37, 53]
gender = ['Male', 'Female', 'Female', 'Male']

persons=[]

for i in range(len(names)):
    persons.append((names[i], ages[i], gender[i]))

print(persons)
# the same can be done by using zip

zipped = zip(names, ages, gender)
persons_list = list(zipped)

print(persons_list)

# a dictionary with key value pairs of names and age can be done by 
ages = dict(zip(names, ages))
print(ages)

# 4. use f string to easily print to console

wish = 'Hi'
print('wish = ', wish)

# or to print on console
# print(f"{wish=}")
