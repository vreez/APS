arr = list(map(int, input().split()))
new = sorted(arr, reverse=True)
for i in range(10):
    print(new[i], end=" ")