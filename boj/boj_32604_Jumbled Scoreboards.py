n = int(input())
q,p = 0, 0
flag = True
for i in range(n):
    a, b = map(int, input().split())
    if a >= q and b >= p:
        q = a
        p = b
    else:
        flag = False

if flag:
    print("yes")
else:
    print("no")