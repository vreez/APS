import sys; sys.stdin = open("18330.txt", "r")

n = int(input())
k = int(input())

if k + 60 > n:
    result = n * 1500
else:
    result = ((k + 60) * 1500) + ((n - (k + 60)) * 3000)

print(result)