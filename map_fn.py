# map() function returns a map object(which is an iterator) of the results after applying 
# the given function to each item of a given iterable (list, tuple etc.)
# i.e.  map(function, iter)
# where iter is an iterable like list, tuple etc

# Returns a list of the results after applying the given function  
# to each item of a given iterable (list, tuple etc.) 

# The returned value from map() (map object) then can be passed to functions like list() 
# (to create a list), set() (to create a set).

# eg. 1

def add_fn(n):
    return n+n 

numbers = (1, 2, 3, 4)
result = map(add_fn, numbers)
print(list(result))

# eg. 2
# using map and lambda
result = map(lambda n: n+n, numbers)
print(list(result))

# eg. 2
# Add two lists using map and lambda
  
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))