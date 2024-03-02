import sys; sys.stdin = open("13496.txt", "r")

K = int(input())
for i in range(K):
    n, s, d = map(int, input().split())
    ans = 0
    for j in range(n):
        di, vi = map(int, input().split())
        if s * d >= di:
            ans += vi
    print("Data Set {}:".format(i+1))
    print(ans)
    print()
