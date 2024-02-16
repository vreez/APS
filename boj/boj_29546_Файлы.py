import sys; sys.stdin = open("29546.txt", "r")

n = int(input())
arr = []
for i in range(n):
    file = input()
    arr.append(file)
m = int(input())
for j in range(m):
    a, b = map(int, input().split())
    for k in range(a-1, b):
        print(arr[k])