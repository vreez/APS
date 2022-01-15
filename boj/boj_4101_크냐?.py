import sys; sys.stdin = open("4101.txt", "r")

while True:
    A, B = map(int, input().split())
    if A == B and A == 0:
        break
    else:
        if A > B:
            print("Yes")
        else:
            print("No")