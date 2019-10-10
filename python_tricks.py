# In-Place Swapping Of Two Numbers.
x, y = 10, 20
print(x, y)
y, x = x, y
print(x, y)

# Reversing a string in Python

a = "Tomorrow Never Dies"
print("Reverse is", a[::-1]) 

# Create a single string from all the elements in list

a = ["How", "Are", "You"] 
print(" ".join(a)) 

# Chaining Of Comparison Operators.
n = 10
result = 1 < n < 20
print(result) 
result = 1 > n <= 9
print(result) 

# Find The Most Frequent Value In A List.
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
print(max(set(test), key = test.count)) 