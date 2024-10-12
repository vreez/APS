import sys; sys.stdin = open("20124.txt", "r")

N = int(input())
res = []
for i in range(N):
    name, score = input().split()
    res.append([int(score), name])

new = sorted(res, key=lambda x : (-x[0], x[1]))
print(new[0][1])