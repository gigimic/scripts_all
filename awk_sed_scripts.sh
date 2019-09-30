#! /bin/bash

# awk commands

# printing all lines from a file
# awk '{ print }' test.txt
# prints first column of all lines from a file
# awk '{ print $1 }' test.txt
# awk '{ print $1, $2}' test.txt # prints the first and second column
# awk '{ print $1.$2}' test.txt #concatenate col 1 and col2
# awk '{ print $NF; }' test.txt #prints the last column
# awk '{ print $(NF-1); }' test.txt #prints the second last column
# awk '/test/ { print }' test.txt # prints lines contains 'test'
# awk '/[a-z]/ { print }' test.txt # prints lines contains any lower case'
# awk '/[0-9]/ { print }' test.txt # prints lines contains any number
# awk '/^[0-9]/ { print }' test.txt # prints lines that start with any number
# awk '/[0-9]$/ { print }' test.txt # prints lines that ends with any number
# awk '{ if($1 ~ /all/ ) print }' test.txt # prints lines that starts with 'all'
# awk '{ if($2 ~ /[0-9]/ ) print }' test.txt # prints lines where col 2 is a number
# grep -i test test.txt | awk '/[0-9]/ { print }' #from all lines containing test, select lines with numbers
# awk -F: '{ print $2 }' test.txt #prints columns after the : in every line
# ls -al | awk -F ":" '{ print $1 }' #applying the above trick to ls -al
# cat test.txt | awk '/test/'
# cat test.txt | awk '$1 ~ /all/'

# sed commands

# cat test.txt | sed -r '' #prints everything from the test file
# cat test.txt | sed -r '2,4d' #prints everything except lines 2:4
# cat test.txt | sed -n -r '2,4p' #prints everything in lines 2:4
cat test.txt | sed -r '/test/d' #prints lines except test
cat test.txt | grep test #same as above
cat test.txt | sed -n -r '/test/p' #prints lines with 'test'
cat test.txt | sed -r 's/test/test1/' #replace test with test1. 
# This substitutes the first occurrence of test in a line. 
# The rest of the test string remain unchanged
cat test.txt | sed -r 's/test/test1/g' # Now it is done globally
cat test.txt | sed -r '2,4 s/test/test1/g' # Now only on lines 2:4
cat test.txt | sed -r '3,$ s/test/test1/g' # Now only on lines 3 to end of file
sed G test.txt #insert a blank line after each line
sed 'G;G' test.txt #inset two blank lines
# More useful commands can be found at the following link
# https://www.geeksforgeeks.org/sed-command-linux-set-2/