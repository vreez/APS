arr = list(input().split())
li = {}
for i in range(len(arr)):
    if arr[i] in li:
        li[arr[i]] += 1
    else:
        li[arr[i]] = 1
num = int(input())

for key, value in li.items():
    if value == num:
        print(key)