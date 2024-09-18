import sys; sys.stdin = open("28635.txt", "r")

m = int(input())
a = int(input())
b = int(input())

if a == b:
    print(0)
elif a > b:
    print(m-a+b)
else:
    print(b-a)