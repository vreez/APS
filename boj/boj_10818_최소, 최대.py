import sys; sys.stdin = open("10818.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

minN = min(arr)
maxN = max(arr)

print(minN, maxN)

