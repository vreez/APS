import sys; sys.stdin = open("19602.txt", "r")

S = int(input())
M = int(input())
L = int(input())

result = (1 * S) + (2 * M) + (3 * L)
if result >= 10:
    print('happy')
else:
    print('sad')