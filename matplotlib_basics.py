from matplotlib import pyplot as plt 
import csv
from pandas import read_csv

plt.style.use('fivethirtyeight')

minutes = list(range(1,10))

# player1 = [1, 2, 3, 3, 4, 4, 4, 4, 5]
# player2 = [1, 1, 1, 1, 2, 2, 2, 3, 4]
# player3 = [1, 1, 1, 2, 2, 2, 3, 3, 3]

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

# plt.pie([1, 1, 1], labels = ["player 1", "player 2", "player 3"])
labels = ["player 1", "player 2", "player 3"]
colors = ['#6d904f', '#fc4f30', '#008fd5']
figa = plt.figure(num=1)
plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))
plt.title('It is a stack plot')
plt.tight_layout()
plt.show()

url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(url, names=names)

data1 = dataset.values

print(dataset.groupby('class').size())
types = dataset.groupby('class').groups.keys()

type_classes= [type for type in types]

data_class = [dataset.groupby('class').groups[type_class] for type_class in type_classes] 

ser = range(len(data_class[0]))
markers =['^', 'o', 's', 'x']
fig = plt.figure(num=2)
grid_no=221
for j in range(3):
	ax1 = fig.add_subplot(grid_no)
	for i in range(4):
		ax1.scatter(ser, data1[data_class[j],i], marker=markers[i], label = names[i])
		if (j == 0): plt.legend()
	grid_no+=1
plt.show()

