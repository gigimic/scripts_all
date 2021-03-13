# Types of iterators provided by itertools

# 1. count(start, step)
# 2. cycle(iterable)
# 3. using next 
# 4. repeat(value, num)

# 1. count(start, step)
import itertools

for i in itertools.count(5,5):
    if i > 25:
        print('condition satisfied')
        break
    else:
        print(i, end = " ")

# 2. cycle(iterable)
count =0
for i in itertools.cycle('ABC'):
    if count > 8:
        print('condition satisfied')
        break
    else:
        print(i, end = " ")
        count += 1

count = 0
num = '123'
for i in itertools.cycle(num):
    if count >=  len(num):
        print('condition satisfied')
        break
    else:
        print(i, end = " ")
        count += 1

# 3. using next

l= ['Hi', 'Hey', 'Hello']
members = itertools.cycle(l)
for i in range(7):
    print(next(members), end = " ")

# 4. repeat(value, num)
print('\n', 'printing repeatedly..........')
print(list(itertools.repeat(10, 5)))

x = iter('123')
print(next(x))
print(next(x))
print(next(x))

