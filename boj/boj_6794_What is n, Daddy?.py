import sys; sys.stdin = open("6794.txt", "r")

N = int(input())
answer = 0
if N == 1 or N == 9 or N == 10:
    print(1)
elif N == 2 or N == 3 or N == 7 or N == 8:
    print(2)
else:
    print(3)
