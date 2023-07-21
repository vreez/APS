import sys; sys.stdin = open("14013.txt", "r")

x, y = map(float, sys.stdin.readline().split())
N = int(sys.stdin.readline())
for i in range(N):
    p, q = sys.stdin.readline().split()
    if q == "A":
        ans = y * float(p) / x
    elif q == "B":
        ans = x * float(p) / y

    print("{:.5f}".format(ans))