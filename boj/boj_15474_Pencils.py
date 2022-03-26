import sys; sys.stdin = open("15474.txt", "r")

N, A, B, C, D = map(int, input().split())

a1 = N // A
if N % A != 0:
    a1 += 1
a2 = N // C
if N % C != 0:
    a2 += 1

if (a1 * B) > (a2 * D):
    print(a2 * D)
else:
    print(a1 * B)



