import sys; sys.stdin = open("28061.txt", "r")

N = int(input())
trees = list(map(int, input().split()))

maxNum = 0
for i in range(N):
    num = trees[i] - (N-i)
    if num > maxNum:
        maxNum = num

print(maxNum)