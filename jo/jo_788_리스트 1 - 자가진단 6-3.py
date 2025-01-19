arr = []
for i in range(1, 16):
    arr.append(i)

n = int(input())
ans = []
for i in range(15):
    if arr[i] % n == 0:
        ans.append(arr[i])
print(ans)