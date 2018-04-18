import numpy as np


DIR = 'DataGenerated/'

def main():

    a = np.random.randint(100, size=(1000, 1000))

    np.savetxt(DIR + "1.csv", a, delimiter=",")
    np.savetxt(DIR + "2.csv", a, delimiter=",")
    np.savetxt(DIR + "3.csv", a, delimiter=",")
    np.savetxt(DIR + "4.csv", a, delimiter=",")
    np.savetxt(DIR + "5.csv", a, delimiter=",")


if __name__ == '__main__':
    main()
    print('Done')