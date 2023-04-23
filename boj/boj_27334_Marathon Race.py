import sys; sys.stdin = open("27334.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
new = sorted(arr)

for i in range(N):
    print(new.index(arr[i])+1)