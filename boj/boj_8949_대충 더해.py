import sys; sys.stdin = open("8949.txt", "r")

A, B = list(input().split())

lenA = len(A)
lenB = len(B)

if lenA > lenB:
    B = '0' * (lenA - lenB) + B

elif lenB > lenA:
    A = '0' * (lenB - lenA) + A

maxLen = max(lenA, lenB)
result = ''
for i in range(maxLen):
    result += str(int(A[i]) + int(B[i]))

print(int(result))