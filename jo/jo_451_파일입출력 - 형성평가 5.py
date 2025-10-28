arr = list(map(int, input().split()))
cnt = 0
li = []
for i in range(len(arr)):
    if arr[i] % 3 == 0 and arr[i] % 5 == 0:
        cnt += 1
        li.append(arr[i])
if cnt == 0:
    print(cnt)
else:
    print(*li)
    print(cnt)