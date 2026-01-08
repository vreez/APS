arr = list(input().split())
ans = {}
for i in range(len(arr)):
    if arr[i] in ans:
        ans[arr[i]] += 1
    else:
        ans[arr[i]] = 1

mx = max(ans.values())
mn = max(ans, key=ans.get)
print("반장은 {}입니다.".format(mn))
print("{}가 받은 표는 {}표입니다.".format(mn, mx))