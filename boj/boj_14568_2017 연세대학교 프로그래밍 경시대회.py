import sys; sys.stdin = open("14568.txt", "r")

N = int(input())
cnt = 0
for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            if (i + j + k) == N and k >= j + 2 and i % 2 == 0:
                cnt += 1
print(cnt)