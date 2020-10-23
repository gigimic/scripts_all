import pandas as pd
# import bar_chart_race as bcr
# bcr.__version__

data = pd.read_csv('covid19.csv', index_col='dateRep', parse_dates=['dateRep'])
# print(data.index)
# print(data.iloc[:10].index)
dates = data.iloc[:10].index

s1 = data.loc[dates[0]]
df2 = pd.DataFrame(columns = [s1.countriesAndTerritories], index = dates)

for date in dates:
    s = data.loc[date]
    df2.loc[date] = [s.cases] 

df2.rename(columns = {"United_States_of_America": "USA", 'United_States_Virgin_Islands': 'USVI'}, inplace = True) 

# print(df2.ndim)
print(df2.shape)
print(df2.index)
print(df2.columns)

dates3 = df2.iloc[:3].index
# print(dates3.shape)
# dates_only3 = dates3.index
print(dates3)

import matplotlib.pyplot as plt

colors = plt.cm.Dark2(range(6))

def nice_axes(ax):
    ax.set_facecolor('.8')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='white')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]
    
fig, ax_array = plt.subplots(nrows=1, ncols=3, figsize=(7, 2.5), 
                             dpi=144, tight_layout=True)
dates = ['01/10/2020', '25/09/2020', '20/09/2020']
for ax, date in zip(ax_array, dates3):
    s2 = df2.loc[date].sort_values(axis = 1, ascending=False)
    print(dates3.loc[date].values)
    s = df2.loc[date].sort_values(by=['cases'], axis = 1, ascending=False)
    print(dates3.loc[date].values)
    ax.barh(y=s.index, width=s.values, color=colors)
    print(s.nlargest(5, ['cases']))
    ax.barh(y=s.countriesAndTerritories.iloc[0:6], width=s.cases.iloc[0:6], color=colors)
    ax.barh(y=s.countriesAndTerritories, width=s.cases, color=colors)
    
    ax.set_title(date, fontsize='smaller')
    ax1.set_xlim([0, 100])
    ax.set_xlim([50000, 95000])
    nice_axes(ax)

plt.show()