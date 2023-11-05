import sys; sys.stdin = open("14592.txt", "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

new = sorted(arr, key=lambda x : (-x[0], x[1], x[2]))

print(arr.index(new[0]) + 1)