import sys; sys.stdin = open("25286.txt", "r")

T = int(input())
for i in range(T):
    y, m = map(int, input().split())
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    check = False
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        check = True
    if check == True:
        days[1] = 29
    if m == 1:
        print(y-1, 12, 31)
    else:
        print(y, m-1, days[m-2])


