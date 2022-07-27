import sys; sys.stdin = open("11257.txt", "r")

N = int(input())

for i in range(N):
    num, s, m, t = map(int, input().split())
    if s + m + t >= 55 and s >= (0.3 * 35) and m >= (0.3 * 25) and t >= (0.3 * 40):
        print(num, s + m + t, "PASS")
    else:
        print(num, s + m + t, "FAIL")
