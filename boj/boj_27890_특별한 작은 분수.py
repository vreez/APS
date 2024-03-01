import sys; sys.stdin = open("27890.txt", "r")

x0, N = map(int, input().split())

for i in range(N):
    if x0 % 2 == 0:
        x0 = (x0 // 2) ^ 6
    else:
        x0 = (2 * x0) ^ 6
print(x0)