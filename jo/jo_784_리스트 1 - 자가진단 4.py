import sys; sys.stdin = open("784.txt", "r")

N = int(input())
arr = [1, 2]
arr.append(N)
for i in range(3):
    print(arr[len(arr)-i-1])