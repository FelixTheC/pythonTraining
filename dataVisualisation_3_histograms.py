import matplotlib.pyplot as plt
from random import randint

test_scores = [randint(40,99) for i in range(15)]
x = [x for x in range(len(test_scores))]
#plt.bar(x, test_scores)

bins = [i for i in range(10, 110, 10)]
plt.hist(test_scores, bins, histtype='bar', rwidth=0.8)

plt.show()