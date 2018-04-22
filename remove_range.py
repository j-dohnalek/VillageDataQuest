import numpy as np
import glob
import time
import json
import os

ARR_SIZE = 10
PATH = 'Data/*.csv'
JSON_PATH = 'tmp/*.json'

# If the DELETE_FILE value is between 1-3 the program overides area of ARR_SIZE x ARR_SIZE from all csv files in PATH 
# defined folder with zeros, according to coordinates from JSON_PATH directory coresponding to file name 
# position{DELETE_FILE}.json. 
# If the DELETE_FILE value is None the program overides area of ARR_SIZE x ARR_SIZE from all csv files in PATH 
# defined folder with zeros, according to coordinates from all files in JSON_PATH directory.
DELETE_FILE = 3

def override():
    """
    Overide area of ARR_SIZE x ARR_SIZE square by zeros according to value of
    DELETE_FILE variable
    """
    for csvfile in glob.glob(PATH):
        
        arr = np.loadtxt(open(csvfile, "rb"), delimiter=",")
        for jsonfile in glob.glob(JSON_PATH):

            if DELETE_FILE is None:
                with open(jsonfile) as jfile:
                    data = json.load(jfile)
                x = data[0]['x']
                y = data[0]['y']
                os.remove(jsonfile)
                arr[y-1: (y-1)+ARR_SIZE, x-1:x-1+ARR_SIZE] = np.zeros((ARR_SIZE, ARR_SIZE))

            else:
                if 'position{}'.format(DELETE_FILE) in jsonfile:

                    with open(jsonfile) as jfile:
                        data = json.load(jfile)
                    x = data[0]['x']
                    y = data[0]['y']
                    os.remove(jsonfile)
                    arr[y - 1: (y - 1) + ARR_SIZE, x - 1:x - 1 + ARR_SIZE] = np.zeros((ARR_SIZE, ARR_SIZE))

        np.savetxt(csvfile, arr.astype(int), fmt='%i', delimiter=",")


if __name__ == '__main__':

    start = time.clock()
    override()
    end = time.clock()

    print('Execution Time: %.3fms' % ((end - start) * 1000))
    print('Execution Time: %.3fs' % (end - start))
    print('Execution Completed')
