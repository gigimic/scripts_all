
# lambda funtion

x = lambda a : a + 10
print(x(5))

add = lambda x, y: x + y
print(add(3, 5))

x1 = lambda a, b, c : a + b + c
print(x1(5, 6, 2))

# map function

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))
print(squared)

# filter function
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# reduce function 
# to find the product of a list of numbers

from functools import reduce
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
product = reduce((lambda x, y: x * y), items)
print(product)