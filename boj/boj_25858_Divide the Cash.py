import sys; sys.stdin = open("25858.txt", "r")

n, d = map(int, input().split())
total = 0
arr = []
for i in range(n):
    num = int(input())
    arr.append(num)
    total += num

for i in range(n):
    print(d // total * arr[i])