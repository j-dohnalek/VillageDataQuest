import itertools


def main():
    i = [i for i in range(1, 16 + 1)]

    print(len(list(itertools.combinations(i, 5))))

    for items in itertools.combinations(i, 5):

        for item in range(5):
            print(items[item], " ", end="")
        print()


if __name__ == '__main__':
    main()