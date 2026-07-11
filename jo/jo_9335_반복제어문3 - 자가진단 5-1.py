a, b = input().split()
ans = []
if ord(a) > ord(b):
    for i in range(ord(a), ord(b)-1, -1):
        ans.append(chr(i))
else:
    for i in range(ord(a), ord(b)+1):
        ans.append(chr(i))
print(*ans)
