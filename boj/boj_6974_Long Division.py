import sys; sys.stdin = open("6974.txt", "r")

N = int(input())
for i in range(N):
    first = int(input())
    second = int(input())
    print(first//second)
    print(first%second)
    print()