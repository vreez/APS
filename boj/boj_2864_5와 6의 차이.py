import sys; sys.stdin = open("2864.txt", "r")

A, B = list(input().split())

bigA = int(A.replace('5', '6'))
smallA = int(A.replace('6', '5'))
bigB = int(B.replace('5', '6'))
smallB = int(B.replace('6', '5'))

print(smallA + smallB, bigA + bigB)
