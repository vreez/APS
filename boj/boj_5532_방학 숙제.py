import sys; sys.stdin = open("5532.txt" , "r")

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

resultA = 0
resultB = 0

if A % C > 0 :
    resultA += (A // C + 1)
else:
    resultA += (A // C)

if  B % D > 0 :
    resultB += (B // D + 1)
else:
    resultB += (B // D)

if resultA > resultB:
    print(L - resultA)
else:
    print(L - resultB)