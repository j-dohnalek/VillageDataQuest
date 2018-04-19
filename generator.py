import numpy as np


DIR = 'DataGenerated/'


def main():

    for i in range(20):
        a = np.random.randint(100, size=(1000, 1000))
        np.savetxt(DIR + "resource{}.csv".format(i), a.astype(int), fmt='%i', delimiter=",")


if __name__ == '__main__':
    main()
    print('Done')