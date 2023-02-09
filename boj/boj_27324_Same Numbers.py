import sys; sys.stdin = open("27324.txt", "r")

N = list(input())
if N[0] == N[1]:
    print(1)
else:
    print(0)