import sys; sys.stdin = open("25991.txt", "r")

N = int(input())
arr = list(map(float, input().split()))
total = 0
for i in range(N):
    total += (arr[i]**3)
ans = total ** (1/3)
print(ans)