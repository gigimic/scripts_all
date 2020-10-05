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

df = pd.DataFrame({
    'col1': [s.index],
    'col2': [s.countriesAndTerritories],
    'col3': [s.cases],
    'col4': [s.deaths]
})
print(df.head())


# print(s.cases)
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots(figsize=(4, 2.5), dpi=144)
# colors = plt.cm.Dark2(range(6))
# y = s.index
# width = s.values
# ax.barh(y=y, width=width, color=colors)

# def nice_axes(ax):
#     ax.set_facecolor('.8')
#     ax.tick_params(labelsize=8, length=0)
#     ax.grid(True, axis='x', color='white')
#     ax.set_axisbelow(True)
#     [spine.set_visible(False) for spine in ax.spines.values()]
    
# nice_axes(ax)
# fig