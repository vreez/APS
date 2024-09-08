import sys; sys.stdin = open("17502.txt", "r")

N = int(input())
arr = list(input())

for i in range(N//2):
    if arr[i] == "?":
        arr[i] = arr[N-1-i]
for i in range(N//2):
    if arr[N-1-i] == "?":
        arr[N-1-i] = arr[i]
for i in range(N):
    if arr[i] == "?":
        arr[i] = "a"
for i in range(N):
    print(arr[i], end="")