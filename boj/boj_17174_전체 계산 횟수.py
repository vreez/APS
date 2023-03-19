import sys; sys.stdin = open("17174.txt", "r")

N, M = map(int, input().split())

answer = N
while True:
    if N//M < M:
        answer += N//M
        break
    else:
        answer += (N//M)
        N = N//M

print(answer)