import sys; sys.stdin = open("17466.txt", "r")

N, P = map(int, sys.stdin.readline().split())
total = 1
for i in range(2, N+1):
    total = (total*i)%P
print(total%P)