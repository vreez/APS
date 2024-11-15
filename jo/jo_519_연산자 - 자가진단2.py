import sys; sys.stdin = open("519.txt", "r")

a, b = map(int, input().split())
print(a+100, b%10)