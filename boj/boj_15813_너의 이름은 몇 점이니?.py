import sys; sys.stdin = open("15813.txt", "r")

N = int(input())
name = list(input())
total = 0
for i in range(N):
    total += (ord(name[i]) - 64)

print(total)