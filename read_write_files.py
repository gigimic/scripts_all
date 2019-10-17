f = open("demofile.txt", "r")
print(f.read())

Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))

Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())

Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)