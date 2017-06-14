import matplotlib.pyplot as plt
from random import randint

labels = 'Taxes', 'Overhead', 'Entertainment'

sizes = [25, 32, 12]
colors = ['c','g','m']

plt.pie(sizes, labels=labels, colors=colors, startangle=90, explode=(0.1,0.3,0.1), autopct= '%1.1f%%')

plt.axis('equal')

plt.show()