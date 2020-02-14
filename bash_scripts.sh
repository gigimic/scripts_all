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

# Find a file
find /home/gigi -name calc.py

# Any variable or function can be declared readonly
# Ctrl Z is the suspend command
# pid is obtained as $$
# sleep 10 for sleeping for 10 sec
# man 7 signal 
# SIGINT is Ctrl C
# there is s trap command to trap the signals given

archiving and compressing files:
to compress a file: 
    gzip file
to uncompress:
    gunzip file.gz 

to pack or archive multiple files:
    tar cvf archive.tar file1 file2 ...

Unpacking tar files: 
    tar xvf archive.tar 
Compressed archives (.tar.gz) 
to decompress and unpack:
    gunzip file.tar.gz 
    tar xvf file.tar 
both the above commands can be combined as: 
    zcat file.tar.gz | tar xvf -
    or 
    tar ztvf file.tar.gz

Another compression utility is bzip2 which compresses text file 
more effectively but slowly and creates a .bz2 file.

device files are in the /dev directory
sda1 is a disk device, a type of block device
/dev/null is a character device
named pipes are like character devices
sockets are special purpose interfaces that are frequently 
used for interprocess communication. They are outside the /dev directory
 To find the sysfs location in /dev use the following
 udevadm info --query=all --name=/dev/sda

 dd is useful when working with block and character files
 dd copies data in blocks of a fixed size
 dd if=/dev/zero of=new_file bs=1024 count=1

 Device Name Summary:
 To find the name of a device (especially when partitioning a disk)
 query udevad
 look for the device in the /sys directory
 guess the name from the output of the dmesg command
 check the output of the mount command
 run cat /proc/devices to see the block and character devices for which 
 the system currently has drivers

 hard disks: /dev/sd* 
 most hard disks correspond to device names such as
 /dev/sda  /dev/sdb etc.
 kernel makes separate device files for partitions on the disk as:
 /dev/sda1  /dev/sda2 etc.

 cd and dvd drivers:
 /dev/sr* devices are read only
 /dev/sg0 represents write and rewrite capabilitites

 PATA hard disks: /dev/hd*
 /dev/hda /dev/hdb /dev/hdc /dev/hdd
 
Terminals: /dev/tty*, /dev/pts/*, and /dev/tty
/dev/tty1  the first virtual console
/dev/pts/0  the first pseudoterminal device
/dev/pts  directory is a dedicated file system 

serial ports: /dev/ttyS*
names of USB serial adapters are
/dev/ttyUSB0 /dev/ttyUSB1
/dev/ttyACM0  /dev/ttyACM1 

parallel ports: /dev/lp0 and /dev/lp1
unidirectional parallel port devices are
/dev/lp0  /dev/lp1 correspond to LPT1 LPT2..
you can send files directly to a parallel port connected for printer
The birectional parallel ports are 
/dev/parport0  /dev/parport1 

audio devices
:/dev/snd/*, /dev/dsp  /dev/audio  

device files can be created using the command mknod
usually it is done with devtmpfs and udev

kernel device files: page 79
udev, devtmpfs, udevd operation etc. are complicated 
udevadm 
monitoring devices:
udevadm monitor
udevadm monitor --kernel --subsystem-match=scsi

the driver and interface hierarchy inside the kernel 
page 60 (how linux works: what every superuser should know)

usb storage and scsi: /dev/sdf
SCSI and ATA
Multiple Access Methods for a Single Device
chapter 4: disks and filesystems
