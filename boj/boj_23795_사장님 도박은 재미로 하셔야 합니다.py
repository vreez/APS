import sys; sys.stdin = open("23795.txt", "r")

total = 0
while True:
    N = int(input())
    if N == -1:
        break
    else:
        total += N

print(total)