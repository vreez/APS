import sys; sys.stdin = open("32216.txt", "r")

n, k, T = map(int, input().split())
d = list(map(int, input().split()))
check = [T] + [0] * n
for i in range(n):
    if check[i] > k:
        check[i+1] = check[i] + d[i] - abs(check[i]-k)
    elif check[i-1] < k:
        check[i+1] = check[i] + d[i] + abs(check[i]-k)
    else:
        check[i+1] = check[i] + d[i]

ans = 0
for i in check[1:]:
    ans += abs(i-k)
print(ans)