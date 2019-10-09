s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

def upper_case_string(astring:str):
    '''
    >>> upper_case_string(sample_string)
    'HOW MANY SATELLITES FOR JUPITER'
    >>> upper_case_string('Your Name')
    'YOUR NAME'

    '''
    upper_string = astring.upper()
    return upper_string


astring = "What is the diameter of moon?"

upper_string = upper_case_string(astring)
print(upper_string)
# to print the doc string of the function
print(upper_case_string.__doc__) 



if __name__ == "__main__":
    import doctest
    sample_string = "How many satellites for Jupiter"
    doctest.testmod(name ='upper_case_string', verbose = True)
    # extraglobs={'sample_string': sample_string})

