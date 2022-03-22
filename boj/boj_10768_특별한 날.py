import sys; sys.stdin = open("10768.txt", "r")

M = int(input())
D = int(input())

if M < 2:
    print("Before")
elif M == 2:
    if D < 18:
        print("Before")
    elif D == 18:
        print("Special")
    else:
        print("After")
else:
    print("After")