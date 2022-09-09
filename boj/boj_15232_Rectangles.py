import sys; sys.stdin = open("15232.txt", "r")

R = int(input())
C = int(input())

for i in range(R):
    for j in range(C):
        print("*", end="")
    print()