import sys; sys.stdin = open("32209.txt", "r")

Q = int(input())
check = 0
for i in range(Q):
    x, y = map(int, input().split())
    if x == 1:
        check += y
    else:
        if check - y >= 0:
            check -= y
        else:
            check -= y
            break
if check >= 0:
    print("See you next month")
else:
    print("Adios")