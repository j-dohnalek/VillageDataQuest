# https://stackoverflow.com/questions/4315506
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.dstack.html
# https://stackoverflow.com/questions/4913397/how-to-add-value-to-a-tuple
# https://stackoverflow.com/questions/37142135
# https://stackoverflow.com/questions/652291
# https://stackoverflow.com/questions/24474522

# sum_tricky Algorithm for seaching N x N subsquare
# https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

import glob
import itertools
import time
import json
import numpy as np


PATH = 'Data/*.csv'


# Size of the side of the array (1000x1000 in actual competition)
ARRAY_SIZE = 1000

# Size of a side of a sub array
SUB_ARRAY_SIZE = 10

# Find N overlapping highest values
FIND_N_HIGHEST = 35

# Filter N unique  non-overlapping values
FILTER_N_HIGHEST = 3

# CLASS ################################################################


class Point:
    """
    Define X, Y point
    https://stackoverflow.com/questions/40795709
    """
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord


class Square:
    """
    Define a square
    https://stackoverflow.com/questions/40795709
    """
    def __init__(self, top_right):
        x = top_right.x - (SUB_ARRAY_SIZE-1)
        y = top_right.y + (SUB_ARRAY_SIZE-1)
        self.bottom_left = Point(x, y)
        self.top_right = top_right

    def intersects(self, other):
        """
        Checking whether two squares overlap
        :param other: Square object
        """
        return not (self.top_right.x < other.bottom_left.x or
                    self.bottom_left.x > other.top_right.x or
                    self.top_right.y > other.bottom_left.y or
                    self.bottom_left.y < other.top_right.y)


class MaximumFinder:
    """ Find the N maximum elements that do not overlap """

    x, y, max = None, None, None

    # Store coordinates of the highest N fields
    containers = {}

    def __init__(self, n_values):
        """
        Initialise the coordinates for N
        :param n_values: consider searching for N maximum values
        :param k: square size
        """
        self.n_values = n_values
        for idx in range(1, self.n_values + 1):
            self.containers[idx] = dict(x=-1, y=-1, max=-1)

    def get_results(self):
        """
        print the top N found value
        :return: void
        """
        return self.containers

    def evaluate(self, x, y, new_sum):
        """
        Set coordinates to consider
        :param x: x coordinates
        :param y: y coordinates
        :param new_sum: value to consider to be the maximum
        """
        self.x = x
        self.y = y
        self.max = new_sum
        self.compute_max()

    def compute_max(self):
        """
        Evaluate the elements on-fly
        """
        bag = self.containers
        old_x, old_y, old_max = 0, 0, 0

        # 1 .. N highest values
        for idx in range(1, self.n_values + 1):

            # Deal with the highest 1st highest value
            if idx == 1 and self.max > bag[idx]['max']:

                old_x, old_y, old_max = bag[idx]['x'], bag[idx]['y'], bag[idx]['max']
                bag[idx] = dict(x=self.x, y=self.y, max=self.max)

            # 2 .. N highest values
            elif idx > 1:
                if old_max > bag[idx]['max']:

                    temp_x, temp_y, temp_max = old_x, old_y, old_max
                    old_x, old_y, old_max = bag[idx]['x'], bag[idx]['y'], bag[idx]['max']
                    bag[idx] = dict(x=temp_x, y=temp_y, max=temp_max)

                else:
                    if self.max >= bag[idx]['max']:
                        if self.max < bag[idx - 1]['max']:

                            old_x, old_y, old_max = bag[idx]['x'], bag[idx]['y'], bag[idx]['max']
                            bag[idx] = dict(x=self.x, y=self.y, max=self.max)

        self.containers = bag

# FUNCTIONS ############################################################


def merge_arrays():
    """
    Merge 2D arrays into one 3D array
    :return: 3D array
    """
    for csvfile in glob.glob(PATH):
        print(csvfile)

    tuple_array = ()
    for csvfile in glob.glob(PATH):

        arr = np.loadtxt(open(csvfile, "rb"), delimiter=",")

        if 'Gold' in csvfile:
            arr = arr * 1

        if 'Oil' in csvfile:
            arr = arr * 1

        if 'Wheat' in csvfile:
            arr = arr * 1

        if 'Iron' in csvfile:
            arr = arr * 1

        tuple_array = tuple_array + (arr,)

    data = np.dstack(tuple_array)
    return data


def sum_tricky(list_2d, n):
    """
    An efficient Python program to find sum of all sub-squares of size k x k in 2D array

    Source:
    https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

    Container data structure: { n: {x, y, max}, .. }

    :param list_2d: 2D array with numbers
    :param n: array width
    :return: n highest identified containers
    """

    maximum_finder = MaximumFinder(FIND_N_HIGHEST)

    k = SUB_ARRAY_SIZE
    # k must be smaller than or equal to n
    if k > n:
        return

    # 1: PRE PROCESSING
    # To store sums of all strips of size k x 1
    strip_sum = [[0] * n for i in range(n)]

    # Go column by column
    for j in range(n):

        # Calculate sum of first k x 1 rectangle in this column
        sum = 0
        for i in range(k):
            sum += list_2d[i][j]
        strip_sum[0][j] = sum

        # Calculate sum of remaining rectangles
        for i in range(1, n-k+1):
            sum += (list_2d[i+k-1][j] - list_2d[i-1][j])
            strip_sum[i][j] = sum

    # 2: CALCULATE SUM of Sub - Squares using strip_sum[][]
    for i in range(n-k+1):
        # Calculate and print sum of first sub square in this row
        sum = 0
        for j in range(k):
            sum += int(strip_sum[i][j])
        maximum_finder.evaluate(j, i, sum)

        # Calculate sum of remaining squares in current row by removing the
        # leftmost strip of previous sub-square and adding a new strip
        for j in range(1, n-k+1):
            sum += int(strip_sum[i][j+k-1] - strip_sum[i][j-1])
            maximum_finder.evaluate(j+k-1, i, sum)

    return maximum_finder.get_results()


def highest_return_combination(obj):
    """
    Compute the highest return combination
    :param obj: data structure containing all data
    """

    maxes_list = []

    # Counting k-combinations (n, k) = n!/(n-k)!k!
    for combo in itertools.combinations([i for i in range(1, FIND_N_HIGHEST + 1)], FILTER_N_HIGHEST):
        sum = 0
        for idx in combo:
            sum += obj[idx]['max']
        maxes_list.append(dict(sum=sum, combo=combo))
    maxes_list.sort(key=lambda item: item['sum'], reverse=True)

    max_sum = -1
    combo = None
    for container in maxes_list:
        current_sum, current_combo = check_for_overlap(obj, container)
        if current_sum > max_sum:
            max_sum = current_sum
            combo = current_combo

    print('--------------------------------')
    print('Maximum Identified: ', max_sum)
    print('Combination: ', combo)
    print('--------------------------------')
    index_number = 1
    for val in combo:
        x2 = obj[val]['x'] - (SUB_ARRAY_SIZE - 1)
        y2 = obj[val]['y']
        print('Square({}) Top Left= x: {}, y: {} Sum:{}'.format(val, x2+1, y2+1, obj[val]['max']))

        with open('tmp/position{}.json'.format(index_number), 'w') as outfile:
            json.dump([dict(x=x2+1, y=y2+1)], outfile)

        index_number += 1

    print('--------------------------------')


def check_for_overlap(obj, data_container):
    """
    Confirm the combination does not contain any overlap
    :param obj:
    :param data_container:
    :return:
    """
    for m in range(FILTER_N_HIGHEST):

        x1, y1 = obj[data_container['combo'][m]]['x'], obj[data_container['combo'][m]]['y']
        square1 = Square(Point(x1, y1))

        for n in range(m + 1, FILTER_N_HIGHEST):

            x2, y2 = obj[data_container['combo'][n]]['x'], obj[data_container['combo'][n]]['y']
            square2 = Square(Point(x2, y2))

            if square1.intersects(square2):
                return 0, ()

    return data_container['sum'], data_container['combo']


# MAIN ############################################################################


if __name__ == '__main__':

    start = time.clock()

    # Generate 5 array of n x n
    data_3d = merge_arrays()

    # Sum the 3D array leaving 2D array
    data_2d = np.sum(data_3d, axis=2)

    # Search for the maximum value
    container = sum_tricky(data_2d.tolist(), n=ARRAY_SIZE)

    # Compute highest return combination
    highest_return_combination(container)

    end = time.clock()

    print('Execution Time: %.3fms' % ((end - start) * 1000))
    print('Execution Time: %.3fs' % (end - start))




