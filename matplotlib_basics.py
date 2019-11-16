from matplotlib import pyplot as plt 

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

plt.stackplot(minutes, player1, player2, player3, labels=labels, colors=colors)

plt.legend(loc=(0.07, 0.05))
plt.title('It is a stack plot')
plt.tight_layout()
plt.show()