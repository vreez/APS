import sys; sys.stdin = open("10991.txt", "r")

N = int(input())

for i in range(1, N+1):
    print(' '*(N-i) + '* '*i)