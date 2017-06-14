import matplotlib.pyplot as plt
from random import randint

test_scores = [randint(40,99) for i in range(35)]
time_spent = [randint(5,60) for i in range(35)]

plt.scatter(time_spent, test_scores)
plt.xlabel('Time spent on test')
plt.ylabel('Test scores')
plt.title('Test score vs Time spent')

plt.show()