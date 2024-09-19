import sys; sys.stdin = open("22966.txt", "r")

N = int(input())
arr = []
for i in range(N):
    a, b = input().split()
    arr.append([b, a])
arr.sort(key=lambda x:int(x[0]))
print(arr[0][1])