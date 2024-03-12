import sys; sys.stdin = open("9297.txt", "r")

X = int(input())
for i in range(X):
    N, D = map(int, input().split())
    print("Case {}:".format(i+1), end=" ")
    if N == 0:
        print("0")
        continue
    if N >= D:
        print(N // D, end=" ")
    if N % D != 0:
        print("{}/{}".format(N % D, D), end="")
    print()