import matplotlib.pyplot as plt

x = [1,3,5,7,10,11]
y = [2,4,15,8,9,3]

y2 = [3,5,13,18,8,7]

plt.bar(x,y, label='One', color='b')
plt.bar(x,y2, label='Two', color='g')

plt.xlabel('bar number')
plt.ylabel('bar height')
plt.title('Bar Chart Tutorial')

plt.legend()
plt.show()