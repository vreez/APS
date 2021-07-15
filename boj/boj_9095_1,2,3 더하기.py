import sys; sys.stdin = open("input/9095.txt", "r")

T = int(input())
for _ in range(T):
    n = int(input())
    def dp(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 4
        return dp(n-1) + dp(n-2) + dp(n-3)
    print(dp(n))

