import sys; sys.stdin = open("21612.txt", "r")

B = int(input())
P = 5 * B - 400

print(P)
if P < 100:
    print(1)
elif P == 100:
    print(0)
else:
    print(-1)
