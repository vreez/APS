import sys; sys.stdin = open("15873.txt", "r")

n = list(input())
l = len(n)

if l == 2:
    print(int(n[0]) + int(n[1]))
elif l == 3:
    if n[1] == '0':
        print(int(n[0] + n[1]) + int(n[2]))
    else:
        print(int(n[0]) + int(n[1] + n[2]))
else:
    print(int(n[0] + n[1]) + int(n[2] + n[3]))