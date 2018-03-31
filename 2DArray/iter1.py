from numpy import genfromtxt
import numpy as np


def rolling_window(a, window):
    shape = a.shape[:-1] + (a.shape[-1] - window + 1, window)
    strides = a.strides + (a.strides[-1],)
    return np.lib.stride_tricks.as_strided(a, shape=shape, strides=strides)


def hwsp(sliding):
    """
    hswp - highest average window of 10 starting position
    running time O(N)
    """
    _max = 0
    _max_pos = 0
    for pos in range(0, 1001):

        if pos + 10 <= 1000:

            avg = sliding[pos].mean()
            if avg > _max:
                _max = avg
                _max_pos = pos
    return _max_pos


def subset_mean(data, x, y):

    if x + 10 > 1000:
        return 0, 0, -1

    if y + 10 > 1000:
        return 0, 0, -1

    # https://stackoverflow.com/questions/30917753
    n1, n2 = np.arange(1000), np.arange(1000)
    b = data[:10, :10]
    b = data[n1[x:x+10, None], n2[None, y:y+10]]
    return x, y, b.mean()


def main():

    data = genfromtxt('foo.csv', delimiter=',')

    # highest average 10 columns starting position
    col = hwsp(rolling_window(data.mean(axis=0), 10))
    # highest average 10 row starting position
    row = hwsp(rolling_window(data.mean(axis=1), 10))

    print('row', row, 'col', col)

    max_average = 0
    max_col = 0
    max_row = 0

    # running time O(N)
    # Seach the highest average column (10 column) for each row
    for y in range(0, 1001):
        coord_row, coord_col, avg = subset_mean(data, col, y)
        if avg > max_average:
            max_average = avg
            max_col = coord_col
            max_row = coord_row

    # running time O(N)
    # Seach the highest average row (10 rows) for each column
    for x in range(0, 1001):
        coord_row, coord_col, avg = subset_mean(data, x, row)
        if avg > max_average:
            max_average = avg
            max_col = coord_col
            max_row = coord_row

    print("max_average", max_average, "row:", max_row, "col:", max_col)


if __name__ == "__main__":
    main()
