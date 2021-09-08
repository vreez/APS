import sys; sys.stdin = open("1181.txt", "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(input())
arr = list(set(arr))
arr = sorted(arr, key = lambda x : (len(x), x))
for i in range(len(arr)):
    print(arr[i])