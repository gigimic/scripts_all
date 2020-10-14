import pandas as pd
# import bar_chart_race as bcr
# bcr.__version__

data = pd.read_csv('covid19.csv', index_col='dateRep', parse_dates=['dateRep'])
# print(data.index)
print(data.iloc[:10].index)
dates = data.iloc[:10].index

s1 = data.loc[dates[0]]
df2 = pd.DataFrame(columns = [s1.countriesAndTerritories], index = dates)

for date in dates:
    s = data.loc[date]
    df2.loc[date] = [s.cases] 

df2.rename(columns = {"United_States_of_America": "USA", 'United_States_Virgin_Islands': 'USVI'}, inplace = True) 

dates3 = data.iloc[:3].index


# print(df2.ndim)
print(df2.shape)
print(df2.index)
# print(df2.columns)