import sys; sys.stdin = open("3578.txt", "r")

N = int(input())
if N == 0:
    print(1)
elif N == 1:
    print(0)
else:
    if N % 2 == 0:
        print("8"*(N//2))
    else:
        print("4"+"8"*(N//2))