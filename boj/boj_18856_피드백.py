import sys; sys.stdin = open("18856.txt", "r")

N = int(input())

arr = [1, 2]
for i in range(3, N):
    arr.append(i)
arr.append(997)

print(N)
for i in range(len(arr)):
    print(arr[i], end=" ")