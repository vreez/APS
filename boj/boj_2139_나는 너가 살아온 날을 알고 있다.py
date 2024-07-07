import sys; sys.stdin = open("2139.txt", "r")
month1 = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
month2 = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
while True:
    d, m, y = map(int, input().split())
    check = False
    if d == 0 and m == 0 and y == 0:
        break
    else:
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    check = True
            else:
                check = True
        ans = 0
        if check == True:
            for i in range(m):
                ans += month1[i]
            ans += d
        else:
            for i in range(m):
                ans += month2[i]
            ans += d
        print(ans)
