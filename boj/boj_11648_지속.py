import sys; sys.stdin = open("11648.txt", "r")

num = list(input())
cnt = 0
while True:
    if len(num) == 1:
        break
    else:
        total = 1
        for i in range(len(num)):
            total *= int(num[i])
        cnt += 1
        num = list(str(total))

print(cnt)
