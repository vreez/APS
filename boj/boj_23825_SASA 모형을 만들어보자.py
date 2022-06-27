import sys; sys.stdin = open("23825.txt", "r")

N, M = map(int, input().split())

if N >= M:
    answer = M // 2
else:
    answer = N // 2

print(answer)