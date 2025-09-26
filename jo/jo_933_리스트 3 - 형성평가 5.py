a, b = map(int, input().split())
arr = [a, b]
for _ in range(8):
    arr.append((arr[-1] + arr[-2])%10)

for i in arr:
    print(i, end=" ")