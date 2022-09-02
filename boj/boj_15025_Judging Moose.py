import sys; sys.stdin = open("15025.txt", "r")

a, b = map(int, input().split())

if a == b and a != 0:
    print("Even {}".format(a*2))
elif a > b or a < b:
    print("Odd {}".format(max(a, b)*2))
else:
    print("Not a moose")
