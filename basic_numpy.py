# Numpy is a general-purpose array-processing package. 
# It provides a high-performance multidimensional array object, 
# and tools for working with these arrays. 
# It is the fundamental package for scientific computing with Python.
# NumPy’s array class is called ndarray. 

import numpy as np

arr1 = np.array([[4, 7], [2, 6]])
arr2 = np.array([[3, 6], [2, 8]])
print(arr1)

# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)

a1 = np.arange(15).reshape(3, 5)
print(a1)
print('Dimension : ', a1.ndim)
print('Shape : ', a1.shape)
print('Type of elements: ', a1.dtype.name)
print('Size in bytes (int64/8)  : ', a1.itemsize)
print('nbytes  : ', a1.nbytes)


print('Sum of elements : ', a1.sum())
print('Min of elements : ', a1.min())
print('Max of elements : ', a1.max())
print('Sum over axis:0 : ', a1.sum(axis = 0))
print('Sum over axis:1 : ', a1.sum(axis = 1))
print('sq. root: ', np.sqrt(a1))

a2 = np.arange( 10, 50, 5)
print('Range of numbers in array : ', a2)
print('last item : ', a2[-1])
print(a2[ : :-1]) #reverse the array
print('every other element : ', a2[::2]) #every other element 
print('first three elements : ', a2[:3])
print('index 3 onwards  : ', a2[3:])
a3 = a2[3:].copy()
print('copy : ', a3)
a4 = np.concatenate([a2, a3])
print('concatenate a2 & a3 : ', a4)
# create an length 10 integer array of zeroes
print(np.zeros(10, dtype =int))
print(np.ones((3,5), dtype=float))
print(np.full((2,3), 2.55))

# trignometric functions
theta  = np.linspace(0, np.pi, 7)
print('theta : ', theta*180/np.pi)
print('sin(theta) : ', np.sin(theta))
print('cos(theta) : ', np.cos(theta))
print('tan(theta) : ', np.tan(theta))

# Exponents and logarithms
a5 = [1, 2, 3]
print("x =", a5)
print("e^x =", np.exp(a5))
print("2^x =", np.exp2(a5))
print("3^x =", np.power(3, a5))

a6 = [1, 2, 4, 10]
print("x =", a6)
print("ln(x) =", np.log(a6))
print("log2(x) =", np.log2(a6))
print("log10(x) =", np.log10(a6))

# broadcasting of arrays in numpy

# arithmetic operations can be done on the array
# a<3 gives a bool array where a is less than 3
# how many values less than 6 in each row or column 
# np.sum(x < 6, axis=1)
