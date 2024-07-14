import sys; sys.stdin = open("30204.txt", "r")

N, X = map(int, input().split())
arr = list(map(int, input().split()))
total = 0
for i in range(N):
    total += arr[i]
if total % X == 0:
    print(1)
else:
    print(0)