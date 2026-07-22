A = []
for i in range(5):
    num = int(input())
    A.append(num)
B = A[:]
C = A[::-1]
print(C)
for i in range(3):
    num = int(input())
    B.append(num)
print(B)
print(A)