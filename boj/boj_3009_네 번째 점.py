import sys; sys.stdin = open("3009.txt", "r")

squareA = {}
squareB = {}
for _ in range(3):
    A, B = map(int, input().split())
    if A not in squareA:
        squareA[A] = 1
    else:
        squareA[A] += 1
    if B not in squareB:
        squareB[B] = 1
    else:
        squareB[B] += 1

for key, value in squareA.items():
    if value == 1:
        print(key, end=" ")

for key, value in squareB.items():
    if value == 1:
        print(key)
