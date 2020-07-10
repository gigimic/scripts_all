def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Symbol must be a single character string.')
    if width <= 2:
        raise Exception('Width must be greater than 2.')
    if height <= 2:
        raise Exception('Height must be greater than 2.')

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

for sym, w, h in (('*', 4, 4), ('O', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print('An exception happened: ' + str(err))



a, b = 10, 20

try :
    if a-b <= 0:
        raise Exception('divide by zero or negative quantity')
    c = a/(a-b)
    print(c)
except Exception as err_msg:
    print('An exception happened: ' + str(err_msg))

# Python displays the traceback whenever a raised exception goes unhandled. 
# But you can also obtain it as a string by calling traceback.format_exc(). 
# This function is useful if you want the information from an exception’s traceback 
# but also want an except statement to gracefully handle the exception. 
# You will need to import Python’s traceback module before calling this function.

# For example, instead of crashing your program right when an exception occurs, 
# you can write the traceback information to a text file and keep your program running. 
# You can look at the text file later, when you’re ready to debug your program.

# logging module is more effective than simply writing this error information to text files.