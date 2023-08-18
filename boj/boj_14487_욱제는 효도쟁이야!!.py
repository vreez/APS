import sys; sys.stdin = open("14487.txt", "r")

n = int(input())
arr = list(map(int, input().split()))

print(sum(arr)-max(arr))