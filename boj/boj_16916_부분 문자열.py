import sys; sys.stdin = open("16916.txt", "r")

P = input()
S = input()

if S in P:
    print(1)
else:
    print(0)