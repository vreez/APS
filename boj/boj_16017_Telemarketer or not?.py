import sys; sys.stdin = open("16017.txt", "r")

A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A == 8 or A == 9:
    if D == 8 or D == 9:
        if B == C:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")
