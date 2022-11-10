import sys; sys.stdin = open("10406.txt", "r")

W, N, P = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0
for i in range(P):
    if arr[i] >= W and arr[i] <= N:
        answer += 1

print(answer)