import sys; sys.stdin = open("30821.txt", "r")

N = int(input())

ans1 = 1
for i in range(N, N-5, -1):
    ans1 *= i
print(ans1 // 120)
