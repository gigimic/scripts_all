import numpy as np
print(np.__version__)

import pandas as pd
import matplotlib.pyplot as plt

# import seaborn as sns
# print(sns.__version__)

data = pd.read_csv('Summer-Olympic-medals-1976-to-2008.csv', encoding='latin-1')
# data.shape
# rows = 15433, columns= 11
# data.head(12)

filt_athlete = data['Athlete'].str.contains('PAES', na = False)
print(data.loc[filt_athlete, ['Athlete', 'Country', 'Medal']])
df = data['Country'].value_counts().sort_values(ascending=False)
top_15 = df[:15]
top_15.plot(kind='bar',figsize=(10,4))
plt.xticks(rotation=75)
plt.title('All Time Medals of top 15 countries')
plt.show()