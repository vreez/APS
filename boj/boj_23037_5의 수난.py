import sys; sys.stdin = open("23037.txt", "r")

n = list(input())

total = 0
for i in range(len(n)):
    total += int(n[i])**5

print(total)