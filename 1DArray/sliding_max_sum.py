# This code is contributed by Shiv Shankar
# https://www.geeksforgeeks.org/sliding-window-maximum-maximum-of-all-subarrays-of-size-k/
# Modified by Jiri Dohnalek


def sliding_max_sum(arr, n, k):
    max = 0
    for i in range(n - k + 1):
        if sum(arr[i: i+k]) > max:
            max = sum(arr[i: i+k])
            print(str(max) + " ", end="")
    print("Max is", str(max))


if __name__=="__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    n = len(arr)
    k = 3
    sliding_max_sum(arr, n, k)
