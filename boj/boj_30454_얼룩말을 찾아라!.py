import sys; sys.stdin = open("30454.txt", "r")

N, L = map(int, input().split())

total = []
for i in range(N):
    arr = list(map(int, input()))
    line = 0
    for j in range(L):
        if j == 0 and arr[j] == 1:
            line += 1
        elif arr[j-1] == 0 and arr[j] == 1:
            line += 1
    total.append(line)

maxNum = max(total)
cnt = 0
for k in range(len(total)):
    if total[k] == maxNum:
        cnt += 1
print(maxNum, cnt)