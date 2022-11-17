import sys; sys.stdin = open("13484.txt", "r")

X = int(input())
N = int(input())
total = X
for i in range(N):
    total += (X - int(input()))
print(total)
