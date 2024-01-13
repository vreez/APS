import sys; sys.stdin = open("8678.txt", "r")

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if b % a == 0:
        print("TAK")
    else:
        print("NIE")