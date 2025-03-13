import sys; sys.stdin = open("750.txt", "r")

a = int(input())
b = int(input())
print("{} / {} = {} ... {}".format(a, b, a//b, a%b))