import sys; sys.stdin = open("9773.txt", "r")

N = int(input())
for i in range(N):
    num = input()
    total = 0
    for i in num:
        total += int(i)
    num2 = int(num[-3:]) * 10
    num3 = total + num2
    if num3 > 9999:
        id = str(num3%10000).zfill(4)
    elif num3 < 1000:
        id = num3 + 1000
    else:
        id = num3

    print(id)
