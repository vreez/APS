import sys; sys.stdin = open("27880.txt", "r")

total = 0
for i in range(4):
    a, b = input().split()
    if a == "Es":
        total += (int(b) * 21)
    elif a == "Stair":
        total += (int(b) * 17)

print(total)