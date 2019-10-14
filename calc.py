def add(x, y):
    return x+y

def divide(x, y):
    ''' Divide function'''
    if y==0:
        raise ValueError('Can not divide by zero')
    
    return x/y
