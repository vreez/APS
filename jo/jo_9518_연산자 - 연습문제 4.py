import sys; sys.stdin = open("9518.txt", "r")

a = int(input())
b = int(input())
c = int(input())

if a > b:
    print("True", end=" ")
else:
    print("False", end=" ")

if b >= c:
    print("True", end=" ")
else:
    print("False", end=" ")

if a <= b:
    print("True", end=" ")
else:
    print("False", end=" ")

if b < c:
    print("True", end=" ")
else:
    print("False", end=" ")