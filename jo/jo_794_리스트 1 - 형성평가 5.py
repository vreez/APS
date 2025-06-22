arr = list(input().split())
new = ['0'] + arr
ans = []
for i in range(len(arr)+1):
    if i != 0 and i % 3 == 0:
        ans.append(new[i])
print(ans)
