num = [100, 100, 200, 100, 100, 200, 200]
print(sum(num))
price=[285.7, 215, 190.05, 166.6, 175, 136.45, 94.7]
amt = [num[i]*price[i] for i in range(len(num))]
print(sum(amt)) 
sell = (400*34.45) + (600*30.1)
loss = sum(amt) - sell
print(loss)
