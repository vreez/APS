import sys; sys.stdin = open("15917.txt", "r")

Q = int(sys.stdin.readline())
arr = [2**i for i in range(32)]
for _ in range(Q):
    N = int(sys.stdin.readline())
    if N in arr:
        print(1)
    else:
        print(0)