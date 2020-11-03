import sys; sys.stdin = open("5205.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    def quickSort(lo, hi):
        if lo >= hi: return

        i, j = lo, hi
        while i < j:
            while i <= hi and arr[lo] >= arr[i]: i += 1
            while arr[lo] < arr[j]: j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[lo], arr[j] = arr[j], arr[lo]

        quickSort(lo, j - 1)
        quickSort(j + 1, hi)


    quickSort(0, len(arr) - 1)
    print("#{} {}".format(tc, arr[N//2]))