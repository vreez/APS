import sys; sys.stdin = open("20673.txt", "r")

p = int(input())
q = int(input())

if p <= 50 and q <= 10:
    print("White")
elif q > 30:
    print("Red")
else:
    print("Yellow")