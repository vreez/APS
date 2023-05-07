import sys; sys.stdin = open("8371.txt", "r")

n = int(input())
first = list(input())
second = list(input())

check = 0
for i in range(n):
    if first[i] != second[i]:
        check += 1
print(check)