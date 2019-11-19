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

snek = """ How long is the snek """
print(snek)

# List Comprehension

numbers = [number for number in range(1,20)]
evens = [number for number in numbers if number % 2 ==0]
list_1 = [number for number in numbers if number %2 == 0 if number >10]
list_2 = [number**2 for number in numbers if number %2 == 0 if number >10]
list_3 = [y*x + " " + z for x in range(3) for y in ['red', 'green'] for z in ['fruit', 'vegetable']]

# List_3 and list_4 are equivalent
list_4 =[]
for x in range(3):
    for y in ['red', 'green']:
        for z in ['fruit', 'vegetable']:
            list_4.append(y*x + " " + z)
# print(list_4)

list_5 = [x**2 +y for x in [number for number in range(5)] for y in [number for number in range(10,12)]]

print(list_5)

