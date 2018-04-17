# https://stackoverflow.com/questions/4315506
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.dstack.html
# https://stackoverflow.com/questions/4913397/how-to-add-value-to-a-tuple
# https://stackoverflow.com/questions/37142135

# sum_tricky Algorithm for seaching N x N subsquare
# https://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/

import glob
import numpy as np
import math

# 5 *.csv files
#PATH = 'Data/*.csv'
PATH = 'Data/gas.csv'
SUB_ARRAY_SIZE = 2


# CLASS ################################################################


# Checking whether two rectangles overlap in python using two bottom left
# corners and top right corners
# https://stackoverflow.com/questions/40795709
class Point:
    """
    Define X, Y point
    """
    def __init__(self, xcoord=0, ycoord=0):
        self.x = xcoord
        self.y = ycoord


class Rectangle:
    """
    Define a rectangle
    """
    def __init__(self, bottom_left, top_right):
        self.bottom_left = bottom_left
        self.top_right = top_right

    def intersects(self, other):
        return not (self.top_right.x < other.bottom_left.x or
                    self.bottom_left.x > other.top_right.x or
                    self.top_right.y < other.bottom_left.y or
                    self.bottom_left.y > other.top_right.y)


class Container:

    def __init__(self, x=SUB_ARRAY_SIZE*(-1), y=SUB_ARRAY_SIZE*(-1), max=-1):
        self.x = x
        self.y = y
        self.max = max
        self.rectangle = Rectangle(Point(x, y),
                                   Point(x + SUB_ARRAY_SIZE, y + SUB_ARRAY_SIZE))

    def update(self, x, y, max, ignore_overlap=False):

        new_rectangle = Rectangle(Point(x, y),
                                  Point(x + SUB_ARRAY_SIZE, y + SUB_ARRAY_SIZE))
        # Check if does not overlap
        if not self.rectangle.intersects(new_rectangle) or ignore_overlap:
            self.x = x
            self.y = y
            self.max = max

            self.rectangle = new_rectangle


class MaximumFinder:
    """
    Find the N maximum elements that do not overlap
    """
    x, y, max = None, None, None

    # Store coordinates of the highest N fields
    containers = []

    def __init__(self, n_values):
        """
        Initialise the coordinates for N
        :param n_values: consider searching for N maximum values
        :param k: square size
        """
        self.n_values = n_values

        for idx in range(1, self.n_values + 1):
            self.containers.append(Container())

    def set_coordinates(self, x, y, new_sum):
        """
        Set coordinates to consider
        :param x: x coordinates
        :param y: y coordinates
        :param new_sum: value to consider to be the maximum
        """
        self.x = x
        self.y = y
        self.max = new_sum

    def evaluate(self):
        """
        Evaluate the elements on-fly
        """
        container = self.containers
        old_x, old_y, old_max = 0, 0, 0

        for idx in range(self.n_values):

            # Consider if the new value is the first highest
            if idx == 0 and self.max > container[idx].max:

                # Store it for comparison in next coming round
                old_x = container[idx].x
                old_y = container[idx].x
                old_max = container[idx].max

                container[idx].update(self.x, self.y, self.max,ignore_overlap=True)

            elif idx > 0:
                pass

        self.containers = container

    def print_result(self):
        """
        print the top N found value
        :return: void
        """
        for idx in range(self.n_values):
            print('sum: {} x: {} y: {}'.format(self.containers[idx].max,
                                               self.containers[idx].x,
                                               self.containers[idx].y))


# FUNCTIONS ############################################################


def merge_arrays():
    """
    Merge 2D arrays into one 3D array
    :return: 3D array
    """
    tuple_array = ()
    for csvfile in glob.glob(PATH):
        tuple_array = tuple_array + (np.loadtxt(open(csvfile, "rb"), delimiter=","),)
    data = np.dstack(tuple_array)
    return data


def sum_tricky(list_2d, n):
    """
    An efficient Python program to find sum of all subsquares of size k x k
    in 2D array
    :param list_2d: 2D array with numbers
    :param n: array width
    :return: void
    """

    maximum_finder = MaximumFinder(2)

    k = SUB_ARRAY_SIZE
    # k must be smaller than or equal to n
    if k > n:
        return

    # 1: PREPROCESSING
    # To store sums of all strips of size k x 1
    strip_sum = [[0 for _ in range(n)] for _ in range(n)]

    # Go column by column
    for j in range(n):

        # Calculate sum of first k x 1
        # rectangle in this column
        sum = 0
        for i in range(k):
            sum += list_2d[i][j]
        strip_sum[0][j] = sum

        # Calculate sum of remaining rectangles
        for i in range(1, n-k+1):
            sum += (list_2d[i+k-1][j] - list_2d[i-1][j])
            strip_sum[i][j] = sum

    # 2: CALCULATE SUM of Sub - Squares
    # using strip_sum[][]
    for i in range(n-k+1):
        # Calculate and print sum of first
        # sub square in this row
        sum = 0
        for j in range(k):
            sum += int(strip_sum[i][j])

        maximum_finder.set_coordinates(i, j, sum)
        maximum_finder.evaluate()
        #print('x: {} y: {} sum: {}'.format(i, j, sum), end="\t")

        # Calculate sum of remaining squares
        # in current row by removing the
        # leftmost strip of previous sub-square
        # and adding a new strip
        for j in range(1, n-k+1):

            sum += int(strip_sum[i][j+k-1] - strip_sum[i][j-1])

            maximum_finder.set_coordinates(i, j+k-1, sum)
            maximum_finder.evaluate()

            #print('x: {} y: {} sum: {}'.format(i, j+k-1, sum), end="\t")
        #print()

    print()
    maximum_finder.print_result()


# MAIN ############################################################################


if __name__ == '__main__':

    # Generate 5 array of n x n
    data_3d = merge_arrays()

    # Sum the 3D array leaving 2D array
    data_2d = np.sum(data_3d, axis=2)

    # Search for the maximum value
    sum_tricky(data_2d.tolist(), n=10)

