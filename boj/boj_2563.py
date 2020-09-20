T = int(input())
color = [list(map(int, input().split())) for _ in range(T)]
paper = [[0] * 100 for _ in range(100)]


for i in range(T):
    for n in range(10):
        for m in range(10):
            paper[color[i][0] + n][color[i][1] + m] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if paper[i][j] == 1:
            cnt += 1
print(cnt)










