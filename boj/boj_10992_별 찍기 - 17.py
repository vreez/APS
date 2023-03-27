import sys; sys.stdin = open("10992.txt", "r")

N = int(input())

for i in range(1, N+1):
    if i == N:
        print("*" * (2*i-1))
    else:
        if i == 1:
            print(" " * (N - i) + "*")
        else:
            print(" "*(N - i) + "*" + " "*(((i - 1) * 2) - 1)+"*")