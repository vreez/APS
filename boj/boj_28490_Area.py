import sys; sys.stdin = open("28490.txt", "r")

N = int(input())
arr = []
for i in range(N):
    h, w = map(int, input().split())
    arr.append(h*w)

print(max(arr))