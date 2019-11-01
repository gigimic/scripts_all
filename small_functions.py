
# lambda funtion

x = lambda a : a + 10
print(x(5))

add = lambda x, y: x + y
print(add(3, 5))

x1 = lambda a, b, c : a + b + c
print(x1(5, 6, 2))

# map function

items = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, items))
# squared = list(map(lambda x: x**2, for i in range(1, 4))
# print(squared)

# filter function
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# Select the odd number from the list and multiply it by 5
x = [2, 3, 4, 5, 6]
y = list(map(lambda x: x*5, filter(lambda x: x%2, x)))
print('yy : ',y)

# reduce function 
# to find the product of a list of numbers

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# product = reduce((lambda x, y: x * y), items)
print(product)

x1 = [2, 3, 4]
y1 = [4, 5]
z1 = list(map(lambda x: list(map(lambda y: x+y, y1)), x1))
print(z1)
z2 = sum(z1,[])
print(z2)
z3 = list(map(lambda z1: [item for sublist in z1 for item in sublist]))
print(z3)