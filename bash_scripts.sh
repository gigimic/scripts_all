#!/bin/bash
# comment
echo "my bash version is   ${BASH_VERSION}"
echo "my script name is    ${BASH_SOURCE[0]}"


if [[ "${BASH_SOURCE[0]}" == "${0}" ]]
then
  echo "${BASH_SOURCE[0]} ${0}"
  echo "${0} gives you the script name"
fi
echo "source file name will read and execute the file"
echo "-----------"
echo "LSB( Linux Standard Base) information about the Linux distribution. Use command lsb_release -a"
lsb_release -a
echo "-----------"
# echo "$1 $2 are the arguments given to the script"
echo "use bc for basic arithmetic operations"

echo "set -x and set +x can be used for debugging the script"
echo "RESOURCES:    shell scripting tutorial"
echo "https://www.youtube.com/user/ProgrammingKnowledge/playlists"

echo "cat /etc/shells  gives you the valid login shells of your machine"
echo testing
echo testing    Hello     # spaces are ignored here
echo "testing    Hello"     # spaces are not ignored here

my_string="How are you"   #No spaces around =

echo "What  is your  name"   #No spaces around =
#read my_name              #This is to read from the prompt
#echo "Hello $my_name $my_string"

echo "Where are \"you\" "

xy=10
if [ $xy -lt 100 ] ; then
    echo "x is less than 100 "; 
else
    echo "x is greater than 100"
fi

count=1
echo $count
count="$((count+1))"
echo $count
count=$count+1
echo $count

echo "MYVAR is: $MYVAR"
MYVAR="hi there"
echo "MYVAR is: $MYVAR"

if [ -f "README.md" ]; then
    echo "file readme exists"
fi

if [ -d "newdir" ]; then
    echo "folder newdir exists"
else   
    echo "folder newdir does not exists"
fi

# Read lines from a file
# while IFS= read -r line
# do
#     echo "$line" 
# done < "README.md"

echo "function to find file exists or not"
# Run the script with argument as filename, and you get the 
# return file exists or not
# The command $# gives the total number of arguments

usage(){
    echo "You need to provide an argument: "
    echo "usage : $0 file_name"
}

does_file_exist() {
    local file="$1"
    [[ -f "$file" ]] && return 0 || return 1
}

#if you dont give an argument, i.e. the length of the arguments is zero usage gets called
[[ $# -eq 0 ]] && usage

if( does_file_exist "$1") then
    echo "File found"
else
    echo "File not found"
fi

# Find a file in a directory
find /home/gigi -name calc.py

# Any variable or function can be declared readonly
# Ctrl Z is the suspend command
# pid is obtained as $$
# sleep 10 for sleeping for 10 sec
# man 7 signal 
# SIGINT is Ctrl C
# there is s trap command to trap the signals given

# archiving and compressing files:
# to compress a file: 
#     gzip file
# to uncompress:
#     gunzip file.gz 

# to pack or archive multiple files:
#     tar cvf archive.tar file1 file2 ...

# Unpacking tar files: 
#     tar xvf archive.tar 
# Compressed archives (.tar.gz) 
# to decompress and unpack:
#     gunzip file.tar.gz 
#     tar xvf file.tar 
# both the above commands can be combined as: 
#     zcat file.tar.gz | tar xvf -
#     or 
#     tar ztvf file.tar.gz

# Another compression utility is bzip2 which compresses text file 
# more effectively but slowly and creates a .bz2 file.