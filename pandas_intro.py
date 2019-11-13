# pandas is like Excel in Python: it uses tables (namely DataFrame) 
# and operates transformations on the data
import numpy as np
import pandas as pd

print('Pandas version is : ', pd.__version__)

# Reading data
# data = pd.read_csv('my_file.csv')

# sep means separator.  nrows=1000 means reading the first 1000 rows. 
# skiprows=[2,5] means you will remove the 2nd and 5th row when reading the file

# data = pd.read_csv('my_file.csv', sep=';',  nrows=1000, skiprows=[2,5])

# The most usual functions: read_csv, read_excel
# Some other great functions: read_clipboard, read_sql

# writing data
# data.to_csv('my_new_file.csv', index=None)

# .to_excel, .to_json, .to_pickle are also available

# data.shape # gives (#rows, #columns)
# data.describe() # computes basic statistics
# data.head(3) # Print the first 3 rows of the data. Similarly .tail() will look at the last rows of the data
# data.loc[8] # prints the 8th row
# data.loc[8, 'col_1'] # prints the value of 8th row in col-1
# data.loc[range(4,6)] # subset from row 4 to 6
# #following can be used to generate subsets
# data[(data['column_1']=='french') & (data['year_born']==1990) & ~(data['city']=='London')]
# data['column_1'].map(len) # The len() function is applied to each element of the ‘column_1’
# data['column_1'].map(len).map(lambda x: x/100).plot() #chaining method
# data.apply(sum) 
# # .apply() applies a function to columns. 
# Use .apply(, axis=1) to do it on the rows.

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
print('data with alphets as indexes: \n', data)

data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['2', '5', '3', '7'])
print('data with numerical indexes: \n', data)

# pandas series can be generated from a python dictionary

#dataframe can be generated from a numpy array
data1 = pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c'])
print(data1)

area = pd.Series({'California': 423967, 'Texas': 695662, 'New York': 141297, 
'Florida': 170312, 'Illinois': 149995})
pop = pd.Series({'California': 38332521, 'Texas': 26448193, 'New York': 19651127, 
'Florida': 19552860, 'Illinois': 12882135})
data2 = pd.DataFrame({'area':area, 'pop':pop})
print(data2)
print(data2['area'])
print(data2.area)
data2['density'] = data2['pop'] / data2['area']
print(data2)
print(data2[data2.density > 100])

A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])
print(A + B)
print('To get rid of NaN')
print(A.add(B, fill_value=0))
