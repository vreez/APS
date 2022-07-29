import sys; sys.stdin = open("5554.txt", "r")

total = 0
for i in range(4):
    sec = int(input())
    total += sec

print(total // 60)
print(total % 60)