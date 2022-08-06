import sys; sys.stdin = open("21665.txt", "r")

n, m = map(int, input().split())
original = [list(input()) for _ in range(n)]
input()
new = [list(input()) for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(m):
        if original[i][j] == new[i][j]:
            answer += 1

print(answer)