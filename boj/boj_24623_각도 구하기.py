import sys; sys.stdin = open("24623.txt", "r")

n = int(input())
a = int(input())

answer = round((180 - a / 2) + (a / 2))
print(answer)
