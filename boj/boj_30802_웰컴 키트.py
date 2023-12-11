import sys; sys.stdin = open("30802.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
T, P = map(int, input().split())
Ts = 0
for i in range(6):
    if arr[i] % T == 0:
        Ts += (arr[i] // T)
    else:
        Ts += (arr[i] // T + 1)
print(Ts)
print(N // P, N % P)