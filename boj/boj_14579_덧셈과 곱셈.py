import sys; sys.stdin = open("14579.txt", "r")

a, b = map(int, input().split())
total = 1
for i in range(a, b+1):
    total *= (i*(i+1)//2)

print(total % 14579)