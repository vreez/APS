import sys; sys.stdin = open("9776.txt", "r")

Pi = 3.14159
N = int(input())
res = []
for i in range(N):
    arr = list(input().split())
    if arr[0] == "S":
        V = (4/3)*Pi*(float(arr[1])**3)
    elif arr[0] == "L":
        V = Pi*(float(arr[1])**2)*(float(arr[2]))
    else:
        V = (1/3)*Pi*(float(arr[1])**2)*(float(arr[2]))

    res.append(V)

big = max(res)
print("{:.3f}".format(big))