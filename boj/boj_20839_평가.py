import sys; sys.stdin = open("20839.txt", "r")

A, C, E = map(int, input().split())
X, Y, Z = map(int, input().split())

if A <= X and C <= Y and E <= Z:
    print("A")
elif A / 2 <= X and C <= Y and E <= Z:
    print("B")
elif C <= Y and E <= Z:
    print("C")
elif C / 2 <= Y and E <= Z:
    print("D")
elif E == Z:
    print("E")
