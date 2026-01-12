arr = list(input().split())
new = set(arr)
new = sorted(new)
for i in range(len(new)):
    print(new[i], end=" ")
print()
print(len(new))