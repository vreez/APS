import sys; sys.stdin = open("17530.txt", "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

if arr[0] == max(arr):
    print('S')
else:
    print('N')