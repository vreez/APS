import sys; sys.stdin = open("2523.txt", "r")

N = int(input())

for i in range(1, N+1):
    print("*" * i)
for i in range(N-1, 0, -1):
        print("*" * i)