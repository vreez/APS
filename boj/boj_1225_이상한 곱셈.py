import sys; sys.stdin = open("1225.txt", "r")

A, B = input().split()
total = 0
for i in A:
    for j in B:
        total += (int(i) * int(j))
print(total)