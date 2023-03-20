import sys; sys.stdin = open("17263.txt", "r")

N = int(input())
arr = list(map(int, input().split()))

new = sorted(arr)
print(new[-1])