arr = list(map(int, input().split()))
print(len(arr))
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        print(arr[i] // 2, end=" ")
    else:
        print(arr[i] * 2, end=" ")