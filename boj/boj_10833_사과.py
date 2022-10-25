import sys; sys.stdin = open("10833.txt", "r")

N = int(input())
answer = 0
for i in range(N):
    s, a = map(int, input().split())
    answer += a % s

print(answer)