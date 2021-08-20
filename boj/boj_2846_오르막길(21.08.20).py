import sys; sys.stdin = open("2846.txt", "r")

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    road = []
    total = 0
    for i in range(N-1):
        if arr[i] >= arr[i+1]:
            if total > 0:
                road.append(total)
                total = 0
            continue
        else:
            total += (arr[i+1] - arr[i])
    if total > 0:
        road.append(total)
    if len(road) == 0:
        print(0)
    else:
        print(max(road))
