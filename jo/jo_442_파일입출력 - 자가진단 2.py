arr = list(map(float, input().split()))

ans = round((arr[0] + arr[-1]) / 2, 1)
print(ans)