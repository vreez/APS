import sys; sys.stdin = open("20336.txt", "r")

n = int(input())

li = []
for _ in range(n):
    li.append(input().split())

for menu in li[0]:
    print(menu)