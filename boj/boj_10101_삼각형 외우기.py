import sys; sys.stdin = open("10101.txt", "r")

A = int(input())
B = int(input())
C = int(input())

if A == 60 and A == B and B == C:
    print("Equilateral")
elif A + B + C == 180 and A == B or B == C or C == A:
    print("Isosceles")
elif A + B + C == 180 and A != B and A != C and B != C:
    print("Scalene")
elif A + B + C != 180:
    print("Error")