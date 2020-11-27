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