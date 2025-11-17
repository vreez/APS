N = int(input())
total = 0
for i in range(N):
    q, y = map(float, input().split())
    total += (q*y)
print(total)
