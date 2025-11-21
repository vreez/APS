N = int(input())
check = []
for i in range(1, 10):
    for j in range(1, 10):
        if i * j not in check:
            check.append(i*j)

if 1 <= N <= 9:
    print(1)
else:
    if N <= 81:
        if N in check:
            print(1)
        else:
            print(0)
    else:
        print(0)
