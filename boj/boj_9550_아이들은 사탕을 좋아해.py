import sys; sys.stdin = open("9550.txt", "r")

T = int(input())
for i in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    total = 0
    for j in range(N):
        total += arr[j] // K

    print(total)