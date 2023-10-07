import sys; sys.stdin = open("30224.txt", "r")

N = input()
NL = list(N)
if "7" not in NL:
    if int(N) % 7 != 0:
        print(0)
    else:
        print(1)
else:
    if int(N) % 7 != 0:
        print(2)
    else:
        print(3)