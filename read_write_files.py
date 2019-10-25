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


Read and write csv files
import csv

file_in = 'list.csv'
rows = []
with open(file_in, 'r') as csv_file:
    input_data = csv.reader(csv_file)
    for row in input_data: 
        rows.append(row) 
        # print(row)
csv_file.close()


file_out ='list_books.csv' 
with open(file_out, 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(rows)
csvFile.close()