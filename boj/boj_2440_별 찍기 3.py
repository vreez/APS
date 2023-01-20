import sys; sys.stdin = open("2440.txt", "r")

N = int(input())

for i in range(1, N+1):
    print('*'*(N-i+1))