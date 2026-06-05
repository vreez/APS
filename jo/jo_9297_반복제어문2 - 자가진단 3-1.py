S, E = map(int, input().split())
arr = []
for i in range(S, E+1, 2):
    arr.append(i)
print(*arr)