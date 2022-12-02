import sys; sys.stdin = open("25640.txt", "r")

j = input()
N = int(input())
cnt = 0
for i in range(N):
    mbti = input()
    if j == mbti:
        cnt += 1

print(cnt)