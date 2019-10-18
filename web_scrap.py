import requests
from bs4 import BeautifulSoup

my_url1 = 'https://elitedatascience.com/python-web-scraping-libraries'
my_url2 = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'
my_url3 = 'https://www.niist.res.in/english/category/contact-us'
page = requests.get(my_url3)
contents = page.content


soup = BeautifulSoup(contents, 'html.parser')
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

# table = soup.find('div', attrs = {'id':'eventcldiv'})
table = soup.findAll('div', attrs = {'class':'container'})
print(table.h1.text)
# table1 = table.find('div', attrs = {'id': 'innercontent'})

# table2 = table1.find('div', attrs = {'id': 'innerleft'})
# table3 = table2.find('div', attrs = {'id': 'inntitlehead'})
# print(table3.h1.text)

# print(len(table))
# print(table.text)

# for block in table.findAll('ul'):
#     print(len(block))
#     for row in block.findAll('li'): 
#         # for row in block.findAll('li', attrs = {'class':'sstitle'}): 
#         people = {}
#         people['name'] = row.name
#         print(row.text)
    


# soup.find(id="inntitlehead")