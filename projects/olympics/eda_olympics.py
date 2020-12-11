import numpy as np
print(np.__version__)

import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sns
# print(sns.__version__)

data = pd.read_csv('Summer-Olympic-medals-1976-to-2008.csv', encoding='latin-1')
# data.shape
# rows = 15433, columns= 11
# data.head(10)

filt_athlete = data['Athlete'].str.contains('PAES', na = False)
print(data.loc[filt_athlete, ['Athlete', 'Country', 'Medal']])

# df = data['Country'].value_counts().sort_values(ascending=False)
# top_15 = df[:15]
# top_15.plot(kind='bar',figsize=(10,4))
# plt.xticks(rotation=75)
# plt.title('All Time Medals of top 15 countries')
# plt.show()

medals_country = data.groupby('Year')
y1976 = medals_country.get_group(1976.0)['Country'].agg('count')
# print(y1976)  

# years = data['year'].unique

# medals_country = data.groupby('Year')
# y1976 = medals_country.get_group(1976.0)['Country'].agg('count')
# y1976 = medals_country.get_group(1976.0)[['Country','Medal']]
y1976 = medals_country.get_group(1976.0)['Country']
# print(y1976)  
# y1976.nlargest(10, 'Medal')
# print(medals_country['Medal'].count())
print(y1976.value_counts().head(10))

years = data['Year'].unique()
years = [x for x in years if str(x) != 'nan']

for index, year in enumerate(years):
    per_year = data.groupby('Year')
    year_group = per_year.get_group(year)['Country']
    print(year)
    print(year_group.value_counts().head(3))



# for index, year in enumerate(years):
#     peryear = data[data['Year']==year]
#     yearcountry = peryear['Country'].value_counts().sort_values(ascending=False)
#     yearcountry[:10].plot(kind='bar',figsize=(10,4), legend=False)
#     plt.title(year)
#     plt.xticks(rotation=45)
#     plt.show()
    