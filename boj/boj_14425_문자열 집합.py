import sys; sys.stdin = open("input/14425.txt", "r")

N, M = map(int, input().split())
arr = {input() for _ in range(N)}
check = list(input() for _ in range(M))

count = 0
for i in range(M):
    if check[i] in arr:
        count += 1

print(count)