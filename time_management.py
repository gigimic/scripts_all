import time

def calcProd():
    # Calculate the product of the first 1,000 numbers.
    product = 1
    for i in range(1, 1000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long.' % (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

# If you need to pause your program for a while, call 
# the time.sleep() function and pass it the number of 
# seconds you want your program to stay paused.

for i in range(3):
    print('Tick')
    time.sleep(1)
    print('Tock')
    time.sleep(3)

time.sleep(5)

# Rounding Numbers
now = time.time()
print(now)
print(round(now, 2))

print(round(now, 4))
print(round(now))
