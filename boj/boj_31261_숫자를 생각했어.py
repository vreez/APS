import sys; sys.stdin = open("31261.txt", "r")

a, b = map(int, input().split())
x = ((((a+b)*a)+a)*a)
print(x)