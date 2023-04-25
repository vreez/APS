import sys; sys.stdin = open("27330.txt", "r")

N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))

score = 0
for i in range(N):
    score += arr1[i]
    if score in arr2:
        score = 0

print(score)