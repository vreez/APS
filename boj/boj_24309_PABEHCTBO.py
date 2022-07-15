import sys; sys.stdin = open("24309.txt", "r")

a = int(input())
b = int(input())
c = int(input())

x = (b - c) // a

print(x)