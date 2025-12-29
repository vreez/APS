N, M, A, B = map(int, input().split())

if N * 3 > M:
    ans = (N*3 - M) * A + B
else:
    ans = 0
print(ans)