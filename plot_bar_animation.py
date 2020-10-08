import pandas as pd
# df = pd.read_csv('data/covid19.csv', index_col='date', parse_dates=['date'])

# s = df.loc['2020-03-29']

data = pd.read_csv('covid19.csv', index_col='dateRep', parse_dates=['dateRep'])
# csv_reader = csv.reader(csv_file)
# exampleData = list(csv_reader)
# exampleData
# print(data.head())
s = data.loc['01/10/2020']
# print(s.index, s.countriesAndTerritories, s.cases, s.deaths)
countries = s.countriesAndTerritories
cases = s.cases
print(countries)
print(s.nlargest(5, ['cases']))
# datewise = pd.DataFrame({
#     'countries': [s.countriesAndTerritories],
#     'cases': [s.cases],
#     'deaths': [s.deaths]
# })

# sorted=datewise.sort_values(by=['cases'])
# print(datewise.sort_values(by=['cases']).loc[:5])
# df.sort_values("col3", axis = 0, ascending = True)
# print(df.head())
# print(df.info(verbose=True))

# print(len(s.countriesAndTerritories))
# print(len(s.cases))

# # print(s.countriesAndTerritories)
# print(s.cases.sort[:2])

# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
# colors = plt.cm.Dark2(range(6))
# y = countries[:10]
# width = cases[:10]
# ax.barh(y=y, width=width, color=colors)
# plt.show()

# def nice_axes(ax):
#     ax.set_facecolor('.8')
#     ax.tick_params(labelsize=8, length=0)
#     ax.grid(True, axis='x', color='white')
#     ax.set_axisbelow(True)
#     [spine.set_visible(False) for spine in ax.spines.values()]
    
# nice_axes(ax)
# fig