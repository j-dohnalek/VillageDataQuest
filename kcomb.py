import time


def main():

    start = time.clock()
    strip_sum = [[0 for _ in range(1000)] for _ in range(1000)]
    end = time.clock()
    print('Time: %.6f miliseconds' % ((end - start) * 1000))

    start = time.clock()
    strip_sum = [[0] * 1000 for _ in range(1000)]
    end = time.clock()
    print('Time: %.6f miliseconds' % ((end - start) * 1000))


if __name__ == '__main__':
    main()