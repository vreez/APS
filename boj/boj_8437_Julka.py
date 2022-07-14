import sys; sys.stdin = open("8437.txt", "r")

total = int(input())
num = int(input())

print((total - num) // 2 + num)
print((total - num) // 2)
