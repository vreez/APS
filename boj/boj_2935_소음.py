import sys; sys.stdin = open("2935.txt", "r")

A = int(input())
cal = input()
B = int(input())

if cal == '+':
    print(A + B)
else:
    print(A * B)
