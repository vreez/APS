import sys; sys.stdin = open("5522.txt", "r")

total = 0
for i in range(5):
    n = int(input())
    total += n

print(total)