A = []
for i in range(5):
    num = int(input())
    A.append(num)

B = A[::-1]
C = B[:]

C.append(int(input()))
print("A = {}".format(A))
print("B = {}".format(B))
print("C = {}".format(C))