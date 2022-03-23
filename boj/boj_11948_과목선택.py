import sys; sys.stdin = open("11948.txt", "r")

first = []
for i in range(4):
    sub = int(input())
    first.append(sub)
second = []
for i in range(2):
    sub = int(input())
    second.append(sub)

first = sorted(first)
second = sorted(second)

total = sum(first) - first[0] + sum(second) - second[0]

print(total)