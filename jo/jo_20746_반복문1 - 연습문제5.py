n = int(input())
ans = 1
for i in range(1, n+1):
    if ans >= n:
        print(i-1)
        break
    else:
        ans *= i
