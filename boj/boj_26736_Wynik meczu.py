import sys; sys.stdin = open("26736.txt", "r")

arr = list(input())
A = 0
B = 0
for i in range(len(arr)):
    if arr[i] == 'A':
        A += 1
    else:
        B += 1

print("{} : {}".format(A, B))