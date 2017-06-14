import matplotlib.pyplot as plt

x = [1,3,5,7,10,11]
y = [2,4,15,8,9,3]

y2 = [3,5,13,18,8,7]

plt.plot(x, y, label='Initial Line')
plt.plot(x, y2, label='New Line')

plt.xlabel('Plot Number')
plt.ylabel('Random #')

plt.title('Epic test graph')

plt.legend()

plt.show()