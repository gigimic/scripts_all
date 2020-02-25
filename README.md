# scripts_all

# understanding scripts

Keep all testing scripts here
These scripts for understanding various small concepts of the python language.

# Web Scraping

Send an HTTP request to the URL.
The server responds to the request by returning the html content of the page.
The library requests is used for this purpose

Then we need to parse the html data.
As html data is nested, string processing cannot be used to extract data.
The libraries used are html5lib, beautifulsoup4(BS4), html.parser,  lxml, selenium, scrapy
BS4 has the ability to automatically detect encodings.
So can be used in documents with special characters.
For e.g. to find all the links in the webpage,
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(contents, 'html.parser')
soup.find_all('a')
'''
lxml is fast and BS4 is used for messy documents

Selenium is more powerful and is mostly used for sites with JavaScript.
It is known as web driver: it can open a google chrome window, visit a site and click on links.

Scrapy is a complete spider that can crawl throgh entire website in a systematic way.
it is a complete webscaping framework. It can be used to manage requests, 
preserve user sessions, follow redirects, and handle output pipelines.

# Python virtual Environment

Create a fresh virtualenv using Python 3:
$ python3 -m venv ./venv

Activating a virtualenv 
source ./venv/bin/activate

insall new libraries to the virtual environment 
(venv) $ pip install requests

install new libraries and add them to the requirements.txt
pip install requests && pip freeze > requirements.txt

To get back to the global Python environment, run the following command:
(venv) $ deactivate