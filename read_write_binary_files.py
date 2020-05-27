# write to a binary file 
f=open("binfile.bin","wb")
num=[5, 10, 15, 20, 25]
arr=bytearray(num)
f.write(arr)
f.close()

# read from a binary file 
f=open("binfile.bin","rb")
num1=list(f.read())
print (num1)
f.close()