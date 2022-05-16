import sys; sys.stdin = open("18005.txt", "r")

N = int(input())

if N % 2:
    print(0)
else:
    if N // 2 % 2:
        print(1)
    else:
        print(2)