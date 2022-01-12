import sys; sys.stdin = open("10039.txt", "r")

total = 0
for _ in range(5):
    score = int(input())
    if score < 40:
        total += 40
    else:
        total += score

print(total // 5)