import sys; sys.stdin = open("17173.txt", "r")

N, M = map(int, input().split())
arr = list(map(int, input().split()))
check = 0
for i in range(1, N+1):
    for num in arr:
        if i % num == 0:
            check += i
            break
print(check)
