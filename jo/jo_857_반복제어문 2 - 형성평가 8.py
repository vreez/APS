n, m = map(int, input().split())

for i in range(n):
    for j in range(m):
        num = i+1
        print(num + (num * j), end=" ")
    print()