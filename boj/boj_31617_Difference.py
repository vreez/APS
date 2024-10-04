import sys; sys.stdin = open("31617.txt", "r")

K = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
ans = 0
for num in A:
    if num + K in B:
        ans += B.count(num+K)
print(ans)