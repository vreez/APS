import sys; sys.stdin = open("input/1120.txt", "r")

A, B = input().split()

result = []
for i in range(len(B) - len(A) + 1):
    total = 0
    for j in range(len(A)):
        if A[j] != B[i + j]:
            total += 1
    result.append(total)
print(min(result))