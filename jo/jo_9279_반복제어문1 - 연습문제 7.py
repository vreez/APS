ans = []
for i in range(1, 501):
    if i % 3 != 0:
        ans.append(i)
    else:
        continue
print(*ans)