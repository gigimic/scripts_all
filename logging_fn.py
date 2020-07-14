import logging
logging.basicConfig(filename = 'loggingProglog.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')
logging.debug('Start of program')

# The filename is added to write the logging details to the file. 

# When you are done with debugging, the following statement 
# can be inserted to disable logging
#  
# logging.disable(logging.CRITICAL) 

# logging message is passed as a string to the following functions. 
# The logging levels are suggestions. you need to decide which category 
# your log message falls into.

logging.debug('Some debugging details.')
logging.info('The logging module is working.')
logging.warning('An error message is about to be logged.')
logging.error('An error has occurred.')
logging.critical('The program is unable to recover!')


def factorial(n):
    logging.debug('Start of factorial(%s%%)'  % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)'  % (n))
    return total

print(factorial(5))
logging.debug('End of program')