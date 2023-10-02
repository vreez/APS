import sys; sys.stdin = open("29736.txt", "r")

A, B = map(int, input().split())
K, X = map(int, input().split())

ans = 0
for i in range(A, B+1):
    if i <= K:
        if (K - i) <= X:
            ans += 1
    else:
        if (i - K) <= X:
            ans += 1
if ans == 0:
    print("IMPOSSIBLE")
else:
    print(ans)