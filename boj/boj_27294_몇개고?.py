import sys; sys.stdin = open("27294.txt", "r")

T, S = map(int, input().split())

if T <= 11 or T > 16 or S == 1:
    print(280)
else:
    print(320)
