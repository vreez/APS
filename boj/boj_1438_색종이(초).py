import sys; sys.stdin = open("1438.txt", "r")

arr = [[0]*100 for _ in range(100)]

N = int(input())
for i in range(N):
    X, Y = map(int, input().split())
    for a in range(X, X+10):
        for b in range(Y, Y+10):
            arr[a][b] = 1

answer = 0
for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            answer += 1

print(answer)
