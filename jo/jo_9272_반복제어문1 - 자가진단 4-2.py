S = int(input())
E = int(input())

li = []
for i in range(S, E-1, -1):
    li.append(i)
print(*li)