import sys; sys.stdin = open("10101.txt", "r")

a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b and b == c and a == 60:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")