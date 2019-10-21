import requests
from bs4 import BeautifulSoup

my_url1 = 'https://elitedatascience.com/python-web-scraping-libraries'
my_url2 = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'
my_url3 = 'https://www.niist.res.in/english/category/contact-us'
page = requests.get(my_url3)
contents = page.content


soup = BeautifulSoup(contents, 'lxml')
# print(soup.prettify())
links = soup.find_all('a')
print(len(links))
text_all = soup.get_text()
# print(text_all)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
# print(soup.p)
# print(soup.p['class'])
# print(soup.find_all('a'))
# for link in soup.find_all('a'):
    # print(link.get('href'))

# for table in soup.find_all('div', id='eventcldiv'):
    # for title in table.find_all('li', class_='sstitle'):
    #     print(title.text)

for table in soup.find_all('div', id='eventcldiv'):
    for title in table.find_all('ul'):
        for addres in title.find_all('li'):
            print(addres.text)
        print()
        