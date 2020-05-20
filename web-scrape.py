# how to do web scraping
# https://automatetheboringstuff.com/2e/chapter12/

# Section 1: opening the web browser
# section 2: downloading a web page with requests
# section 3: saving the downloaded data to the hard drive.

# Section 1
import webbrowser

# webbrowser.open('https://inventwithpython.com/')
print('opened INVENT WITH PYTHON')
# webbrowser.open("https://www.nytimes.com/")
# print('opened NEW YORK TIMES')
# This is a useful piece of code.
# If you begin your online work by opening a bunch of websites, 
# it can be automated using this small piece of code.

# section 2
# details of the requests module can be fount at: https://requests.readthedocs.org/
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
print(res.raise_for_status())
if (res.status_code == requests.codes.ok):
    print(len(res.text))

# checking for errors
res1 = requests.get('https://automatetheboringstuff.com/no_files')
try:
    res1.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print('done')

# This piece of code can automate the regular downloading of data 
# or anything you need to do regularly, which can then be used for analysis.

# Section 3
# saving downloaded data to the hard drive

playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(100000):
        playFile.write(chunk)
playFile.close()

# Even if the page is in plaintext, you need to write binary data 
# instead of text data in order to maintain the Unicode encoding of the text.
# The iter_content() method returns “chunks” of the content on each iteration 
# through the loop. Each chunk is of the bytes data type. 