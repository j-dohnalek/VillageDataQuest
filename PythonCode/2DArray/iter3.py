from numpy import genfromtxt
import numpy as np


def subset_mean(data, x, y):

    if x+10 > 1000 or y+10 > 1000:
        return 0

    # https://stackoverflow.com/questions/30917753
    n1, n2 = np.arange(1000), np.arange(1000)
    b = data[:10, :10]
    b = data[n1[y:y+10, None], n2[None, x:x+10]]
    return b.mean()


max_average = 0
max_col = 0
max_row = 0
data = genfromtxt('foo.csv', delimiter=',')

# running time O(N)
# Seach the highest average column (10 column) for each row
for y in range(0, 1000):
    for x in range(0, 1000):
        avg = subset_mean(data, x, y)
        if avg > max_average:
            max_average = avg
            max_col = x
            max_row = y

print("max_average", max_average, "row:", max_row + 1, "col:", max_col + 1)
