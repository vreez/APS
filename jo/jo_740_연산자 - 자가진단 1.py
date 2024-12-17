import sys; sys.stdin = open("740.txt", "r")

total = 0
for i in range(3):
    num = int(input())
    total += num

print("sum : {}".format(total))
print("avg : {}".format(total // 3))
