import sys; sys.stdin = open("5220.txt", "r")

N = int(input())
for i in range(N):
    num, check = map(int, input().split())
    new = str(bin(num)[2:])
    if new.count('1') % 2:
        if check == 1:
            print("Valid")
        else:
            print("Corrupt")
    else:
        if check == 1:
            print("Corrupt")
        else:
            print("Valid")