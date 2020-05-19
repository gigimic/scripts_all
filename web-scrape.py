# how to do web scraping
# https://automatetheboringstuff.com/2e/chapter12/

# Section 1: opening the web browser
# section 2: downloading a web page with requests

# Section 1
import webbrowser

# webbrowser.open('https://inventwithpython.com/')
print('opened INVENT WITH PYTHON')
# webbrowser.open("https://www.nytimes.com/")
# print('opened NEW YORK TIMES')

# section 2
# details of the requests module can be fount at: https://requests.readthedocs.org/
import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# print(type(res))
print(res.raise_for_status())
if (res.status_code == requests.codes.ok):
    print(len(res.text))

# checking for errors
res = requests.get('https://automatetheboringstuff.com/no_files')
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

print('done')