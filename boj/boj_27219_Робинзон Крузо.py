import sys; sys.stdin = open("27219.txt", "r")

N = int(input())
a = N // 5
b = N % 5
print('V'*a+'I'*b)