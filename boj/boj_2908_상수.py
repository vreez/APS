import sys; sys.stdin = open("input/2908.txt", "r")

A, B = input().split()

numA = list(A)
numB = list(B)

i = 2
while i >= 0:
    if numA[i] > numB[i]:
        print(''.join(reversed(A)))
        break
    elif numB[i] > numA[i]:
        print(''.join(reversed(B)))
        break
    else:
        i -= 1




