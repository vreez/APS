import sys; sys.stdin = open("921.txt", "r")

n = int(input())
arr = []
for i in range(1, n+1):
    arr.append(i**2)
print(arr)