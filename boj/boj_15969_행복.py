import sys; sys.stdin = open("15969.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
print(max(arr) - min(arr))