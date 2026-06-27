a, b = map(int, input().split())
ans = []
if a > b:
    for i in range(b, a+1):
        if i not in ans and i % 3 == 0 or i % 5 == 0:
            ans.append(i)
else:
    for i in range(a, b+1):
        if i not in ans and i % 3 == 0 or i % 5 == 0:
            ans.append(i)

print("CNT: {}".format(len(ans)))
print("SUM: {}".format(sum(ans)))