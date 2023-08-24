import sys; sys.stdin = open("10813.txt", "r")

n, m = map(int, input().split())
arr = [0]
for i in range(1, n+1):
    arr.append(i)

for i in range(m):
    a, b = map(int, input().split())
    imsi = arr[a]
    arr[a] = arr[b]
    arr[b] = imsi

for i in range(1, n+1):
    print(arr[i], end=" ")
