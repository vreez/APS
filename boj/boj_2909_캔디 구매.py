import sys; sys.stdin = open("2909.txt", "r")

C, K = map(int, input().split())
ans = int(round(C+0.1, -K))
print(ans)