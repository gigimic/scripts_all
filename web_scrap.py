import requests
from bs4 import BeautifulSoup
import pandas as pd

my_url1 = 'https://elitedatascience.com/python-web-scraping-libraries'
my_url2 = 'https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/'
my_url3 = 'https://www.niist.res.in/english/category/contact-us'
my_url4 = 'https://www.nytimes.com/books/best-sellers/hardcover-fiction/'
page = requests.get(my_url4)
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

# for table in soup.find_all('div', id='eventcldiv'):
#     for title in table.find_all('ul'):
#         for addres in title.find_all('li'):
#             print(addres.text)
#         print()
best_sellers = []
for lists in soup.find_all('ol', class_='css-12yzwg4'):
    for title in lists.find_all('li'):
        # print(title.prettify())
        # print(title.article.find('h3', class_='css-5pe77f'))
        if(title.article is not None):
            book_details = {}
            book_name = title.article.h3.text
            print(title.article.h3.text)
            book_details['name'] = book_name
            author = title.article.find('p', class_='css-1j7a9fx')
            print(author.text)
            book_details['author'] = author.text
            publisher = title.article.find('p', class_='css-heg334')
            print(publisher.text)
            book_details['publisher'] = publisher.text
            best_sellers.append(book_details)
            print(title.article['itemprop'])
            print()
            # bookData = pd.DataFrame.from_dict(best_sellers)
            # bookData.to_csv('list_best_sellers.csv')
        