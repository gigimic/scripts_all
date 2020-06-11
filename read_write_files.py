f = open("demofile.txt", "r")
print(f.read())

# Return the 5 first characters of the file:
f = open("demofile.txt", "r")
print(f.read(5))

# Read one line of the file:
f = open("demofile.txt", "r")
print(f.readline())

# Loop through the file line by line:
f = open("demofile.txt", "r")
for x in f:
  print(x)


# Read and write csv files
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

# Here exampleData is a list of lists 

csv_file = open('data1.csv')
csv_reader = csv.reader(csv_file)
exampleData = list(csv_reader)
exampleData


# Read pdf files 

import PyPDF2
pdfFileObj = open('filename.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages   #provides the number of pages
pageObj = pdfReader.getPage(0)
pageObj.extractText()
pdfFileObj.close()

# decryption of pdf
# if the pdf document is protected by a password 

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.isEncrypted #provides TRUE if it is encrypted

pdfReader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
pdfReader.decrypt('password')
pageObj = pdfReader.getPage(0)


