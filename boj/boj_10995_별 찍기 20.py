import sys; sys.stdin = open("10995.txt", "r")

N = int(input())

for i in range(N):
    for j in range(N*2):
        if i % 2 == 0 and j % 2 == 0:
            print("*", end="")
        elif i % 2 == 0 and j % 2 != 0:
            print(" ", end="")
        elif i % 2 != 0 and j % 2 == 0:
            print(" ", end="")
        elif i % 2 != 0 and j % 2 != 0:
            print("*", end="")
    print()
