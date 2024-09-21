import sys; sys.stdin = open("21313.txt", "r")

N = int(input())

if N % 2 == 0:
    ans = [1, 2] * (N//2)
else:
    ans = [1, 2] * (N//2) + [3]
print(*ans)
