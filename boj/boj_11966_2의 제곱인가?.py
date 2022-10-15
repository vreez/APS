import sys; sys.stdin = open("11966.txt", "r")

N = int(input())
arr = []
for i in range(31):
    arr.append(2 ** i)
if N in arr:
    print(1)
else:
    print(0)