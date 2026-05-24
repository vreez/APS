a = int(input())
b = int(input())
ans = []
for i in range(b, a+1):
    ans.append(i**2)
print(*ans)