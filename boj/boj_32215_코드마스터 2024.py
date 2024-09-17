import sys; sys.stdin = open("32215.txt", "r")

n, m, k = map(int, input().split())
print(m*(k+1))
