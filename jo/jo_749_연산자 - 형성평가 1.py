import sys; sys.stdin = open("749.txt", "r")

total = 0
for i in range(4):
    score = int(input())
    total += score

print("sum {}".format(total))
print("avg {}".format(total//4))