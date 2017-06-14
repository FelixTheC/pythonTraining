import matplotlib.pyplot as plt
from random import randint

year = [i for i in range(1,11)]
# in thousands :)
taxes = [randint(5, 20) for i in range(1,11)]
overhead = [randint(1, 40) for i in range(1,11)]
entertainment = [randint(10, 50) for i in range(1,11)]

plt.plot([], [], color='m', label='taxes')
plt.plot([], [], color='g', label='overhead')
plt.plot([], [], color='c', label='entertainment')

plt.stackplot(year, taxes, overhead, entertainment, colors=['m','g','c'])

plt.xlabel('Years')
plt.ylabel('Cost, in thousands')
plt.title('Company expanses')

plt.legend()

plt.show()