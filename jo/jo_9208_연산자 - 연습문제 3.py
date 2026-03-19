N = int(input())
A, B = map(int, input().split())

result = []
if N == A:
    result.append("True")
else:
    result.append("False")
if N == B:
    result.append("True")
else:
    result.append("False")
if N != A:
    result.append("True")
else:
    result.append("False")
if N != B:
    result.append("True")
else:
    result.append("False")
print(*result)
