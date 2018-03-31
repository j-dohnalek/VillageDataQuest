from numpy import genfromtxt
import numpy as np


def subset_mean(data, x, y):

    if x + 10 > 1000:
        return x, y, 0

    if y + 10 > 1000:
        return x, y, 0

    # https://stackoverflow.com/questions/30917753
    n1, n2 = np.arange(1000), np.arange(1000)
    b = data[:10, :10]
    b = data[n1[x:x+10, None], n2[None, y:y+10]]
    return x, y, b.mean()


def main():

    data = genfromtxt('foo.csv', delimiter=',')

    max_average = 0
    max_col = 0
    max_row = 0

    # running time O(N)
    # Seach the highest average column (10 column) for each row
    for y in range(0, 1000):
        for x in range(0, 1000):
            coord_row, coord_col, avg = subset_mean(data, x, y)
            if avg > max_average:
                max_average = avg
                max_col = coord_col
                max_row = coord_row

    print("max_average", max_average, "row:", max_row + 1, "col:", max_col + 1)


if __name__ == "__main__":
    main()
