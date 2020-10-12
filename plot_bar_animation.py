import pandas as pd
# df = pd.read_csv('data/covid19.csv', index_col='date', parse_dates=['date'])

# s = df.loc['2020-03-29']

data = pd.read_csv('covid19.csv', index_col='dateRep', parse_dates=['dateRep'])
# csv_reader = csv.reader(csv_file)
# exampleData = list(csv_reader)
# exampleData
# print(data.head())
# s = data.loc['01/10/2020'].sort_values(by=['cases'], ascending=False)
# s = data.loc['01/10/2020']
# print(s.index, s.countriesAndTerritories, s.cases, s.deaths)
# countries = s.countriesAndTerritories
# cases = s.cases
# print(countries)
# print(s.nlargest(5, ['cases']))



import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
colors = plt.cm.Dark2(range(6))
# y = s.countriesAndTerritories[:10]
# width = s.cases[:10]
# ax.barh(y=y, width=width, color=colors)
# plt.show()

# df = pd.DataFrame(columns = ['Name', 'Articles', 'Improved'],  
#                    index = ['a', 'b', 'c']) 

# data.loc['01/10/2020'].cases.rank(method='first')
# datewise = pd.DataFrame() 
dates = ['01/10/2020', '25/09/2020', '20/09/2020']
s1 = data.loc[dates[0]]
df2 = pd.DataFrame(columns = [s1.countriesAndTerritories], index = dates)
# for date in dates:
#     s = data.loc[date]
#     # df2 = pd.DataFrame({'date': date, 'cases': 1})
#     df2.loc[date] = [s.cases] 
#     # datewise.append(df2)

# print(df2)
print(df2.size)

def nice_axes(ax):
    ax.set_facecolor('.8')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='white')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]
    
fig, ax_array = plt.subplots(nrows=1, ncols=3, figsize=(7, 2.5), 
                             dpi=144, tight_layout=True)
# dates = ['01/10/2020', '25/09/2020', '20/09/2020']
for ax, date in zip(ax_array, dates):
    s = data.loc[date].sort_values(by=['cases'], ascending=False)
    # s = data.loc[date].sort_values()
    print(s.nlargest(5, ['cases']))
    ax.barh(y=s.countriesAndTerritories.iloc[0:6], width=s.cases.iloc[0:6], color=colors)
    ax.set_title(date, fontsize='smaller')
    nice_axes(ax)
    s1 = data.loc[date]
    df2.loc[date] = [s1.cases] 

# changing cols with rename() 
df2.rename(columns = {'Afghanistan': 'Af', "United_States_of_America": "USA"}, inplace = True) 

print(df2.ndim)
print(df2.shape)
print(df2.index)
print(df2.columns)
# plt.show()