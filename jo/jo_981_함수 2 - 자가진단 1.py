n = int(input())
arr = list(map(int, input().split()))

def func(arr):
    print(*sorted(arr, reverse=True))
func(arr)