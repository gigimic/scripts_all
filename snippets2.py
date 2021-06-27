# yield instead of return in a function

# The yield statement suspends the execution of the function and 
# returns a value back. When resumed the function continues execution 
# immediately after the yield statement 

# yield is like a generator function

# following is a list and we can use it multiple times
mylist = [x*x for x in range(3)]
for i in mylist:
    print('list ', i)
print(mylist)

# following is a generator and can be used only once
mygenerator = (x*x for x in range(3))
for i in mygenerator:
    print('generator ', i)

# Here you can see that generator is an object
def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

mygenerator = create_generator() # create a generator
# print(mygenerator) # mygenerator is an object!
# <generator object create_generator at 0xb7555c34>
for i in mygenerator:
    print(i)

# yield is also a generator. It is an object 
def fn_sq():
    num = 1
    print('num ', num)
    while num < 5:
        yield num*num
        num+=1
        print('next call of sq function') 

i=[2,4,8]
for i2 in fn_sq():
    print(i2)
    
