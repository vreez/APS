A, T = map(int, input().split())

ans = 10 + 2 * (25 - A + T)

if ans < 0:
    print(0)
else:
    print(ans)