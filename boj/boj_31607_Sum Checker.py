import sys; sys.stdin = open("31607.txt", "r")

A = int(input())
B = int(input())
C = int(input())

arr = [A, B, C]
new = sorted(arr)

if new[0] + new[1] == new[2]:
    print(1)
else:
    print(0)