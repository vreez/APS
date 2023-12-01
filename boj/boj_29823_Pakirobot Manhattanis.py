import sys; sys.stdin = open("29823.txt", "r")

N = int(input())
arr = list(input())
horizon = 0
width = 0
for i in range(N):
    if arr[i] == "N":
        width += 1
    elif arr[i] == "S":
        width -= 1
    elif arr[i] == "E":
        horizon += 1
    else:
        horizon -= 1

ans = abs(horizon) + abs(width)
print(ans)
