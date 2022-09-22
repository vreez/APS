import sys; sys.stdin = open("4766.txt", "r")

arr = []
while True:
    N = float(input())
    if N == 999:
        break
    else:
        arr.append(N)

for i in range(1, len(arr)):
    print(format(arr[i]-arr[i-1], ".2f"))