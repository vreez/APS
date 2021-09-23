import sys; sys.stdin = open("14490.txt", "r")

n, m = input().split(':')

numM = int(m)
numN = int(n)

while numM:
    numN, numM = numM, numN % numM

print("{}:{}".format(int(n) // numN, int(m) // numN))
