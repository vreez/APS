import sys; sys.stdin = open("8826.txt", "r")

K = int(input())
for i in range(K):
    num = int(input())
    arr = list(input())
    N, S, W, E = 0, 0, 0, 0
    ans = 0
    for j in range(num):
        if arr[j] == "N":
            N += 1
        elif arr[j] == "S":
            S += 1
        elif arr[j] == "W":
            W += 1
        else:
            E += 1
    if N == S:
        ans += 0
    else:
        ans += abs(N - S)
    if W == E:
        ans += 0
    else:
        ans += abs(W - E)

    print(ans)
