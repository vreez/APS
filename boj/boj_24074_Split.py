import sys; sys.stdin = open("24074.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

flag = arr.index(max(arr))
if flag == 0:
    print(0)
    print(sum(arr)-arr[flag])
elif flag == (N - 1):
    print(sum(arr)-arr[flag])
    print(0)
else:
    print(sum(arr[:flag]))
    print(sum(arr[flag+1:]))