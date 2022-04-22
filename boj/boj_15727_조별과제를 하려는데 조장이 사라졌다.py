import sys; sys.stdin = open("15727.txt", "r")

N = int(input())

if N % 5 > 0:
    print(N//5 + 1)
else:
    print(N//5)

