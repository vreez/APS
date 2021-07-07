import sys; sys.stdin = open("input/1138.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
result = [0] * N
for i in range(N):
    count = 0
    for j in range(N):
        if result[j] == 0:
            count += 1
        if count - 1 == arr[i] and result[j] == 0:
            result[j] = i + 1

for i in range(N):
    print(result[i], end=' ')