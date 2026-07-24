A = []
for i in range(5):
    num = int(input())
    A.append(num)

first = A[2:]
print(first)
second = first[::-1]
print(second)
print(A[::-1])