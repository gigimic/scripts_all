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

# data.loc['01/10/2020'].cases.rank(method='first')
# dates = ['01/10/2020', '25/09/2020', '20/09/2020']
# datewise ={}
# for date in dates:
#     datewise.date = date

def nice_axes(ax):
    ax.set_facecolor('.8')
    ax.tick_params(labelsize=8, length=0)
    ax.grid(True, axis='x', color='white')
    ax.set_axisbelow(True)
    [spine.set_visible(False) for spine in ax.spines.values()]
    
fig, ax_array = plt.subplots(nrows=1, ncols=3, figsize=(7, 2.5), 
                             dpi=144, tight_layout=True)
dates = ['01/10/2020', '25/09/2020', '20/09/2020']
for ax, date in zip(ax_array, dates):
    s = data.loc[date].sort_values(by=['cases'], ascending=False)
    ax.barh(y=s.countriesAndTerritories.iloc[0:6], width=s.cases.iloc[0:6], color=colors)
    ax.set_title(date, fontsize='smaller')
    nice_axes(ax)

plt.show()