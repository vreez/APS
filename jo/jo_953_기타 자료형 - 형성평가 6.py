arr = list(input().split())

dic = {}
for i in range(len(arr)):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

min_v = min(dic.values())

ans = []
for key, value in dic.items():
    if value == min_v:
        ans.append(key)
for i in range(len(ans)):
    print(ans[i])
print(min_v)