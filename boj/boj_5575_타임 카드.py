import sys; sys.stdin = open("5575.txt", "r")

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

if A[5] >= A[2]:
    As = A[5] - A[2]
else:
    As = A[5] + 60 - A[2]
    A[4] -= 1

if A[4] >= A[1]:
    Am = A[4] - A[1]
else:
    Am = A[4] + 60 - A[1]
    A[3] -= 1

Ah = A[3] - A[0]

if B[5] >= B[2]:
    Bs = B[5] - B[2]
else:
    Bs = B[5] + 60 - B[2]
    B[4] -= 1

if B[4] >= B[1]:
    Bm = B[4] - B[1]
else:
    Bm = B[4] + 60 - B[1]
    B[3] -= 1

Bh = B[3] - B[0]

if C[5] >= C[2]:
    Cs = C[5] - C[2]
else:
    Cs = C[5] + 60 - C[2]
    C[4] -= 1

if C[4] >= C[1]:
    Cm = C[4] - C[1]
else:
    Cm = C[4] + 60 - C[1]
    C[3] -= 1

Ch = C[3] - C[0]

print(Ah, Am, As)
print(Bh, Bm, Bs)
print(Ch, Cm, Cs)
