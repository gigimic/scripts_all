# Numpy is a general-purpose array-processing package. 
# It provides a high-performance multidimensional array object, 
# and tools for working with these arrays. 
# It is the fundamental package for scientific computing with Python.

import numpy as np

arr1 = np.array([[4, 7], [2, 6]])
arr2 = np.array([[3, 6], [2, 8]])
print(arr1)

# Transpose of Array
# using In-built function 'T'
Trans_arr = arr1.T
print("\nTranspose of Array: ")
print(Trans_arr)