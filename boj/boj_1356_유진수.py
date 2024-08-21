import sys; sys.stdin = open("1356.txt", "r")

num = input()
check = False
for i in range(1, len(num)):
    a = num[:i]
    b = num[i:]
    n1 = 1
    n2 = 1
    for n in range(len(a)):
        n1 *= int(a[n])
    for m in range(len(b)):
        n2 *= int(b[m])
    if n1 == n2:
        check = True
        break
if check == True:
    print("YES")
else:
    print("NO")
