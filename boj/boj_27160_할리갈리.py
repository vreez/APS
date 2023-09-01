import sys; sys.stdin = open("27160.txt", "r")

total = [0] * 4

N = int(input())
for i in range(N):
    fruit, num = input().split()
    if fruit == "STRAWBERRY":
        total[0] += int(num)
    elif fruit == "BANANA":
        total[1] += int(num)
    elif fruit == "LIME":
        total[2] += int(num)
    else:
        total[3] += int(num)
if 5 in total:
    print("YES")
else:
    print("NO")