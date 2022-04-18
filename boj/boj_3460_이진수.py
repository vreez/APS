import sys; sys.stdin = open("3460.txt", "r")

T = int(input())
for i in range(T):
    N = int(input())
    b = format(N, 'b')
    B = list(b)
    B.reverse()
    for i in range(len(B)):
        if B[i] == '1':
            print(i, end=" ")



