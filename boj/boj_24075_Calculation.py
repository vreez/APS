import sys; sys.stdin = open("24075.txt", "r")

A, B = map(int, input().split())
maxNum = max(A + B, A - B)
minNum = min(A + B, A - B)

print(maxNum)
print(minNum)