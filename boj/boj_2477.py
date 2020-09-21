'''
7
2 170
3 300
1 200
4 10
2 30
4 290
'''

# 모든 예외 케이스를 다 생각해봐야 한다.

import sys

T = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(6)]

sero = []
garo = []
for i in range(6):
    if arr[i][0] == 1 or arr[i][0] == 2:
        sero.append(arr[i][1])
    else:
        garo.append(arr[i][1])

a, b = 0, 0
for i in range(6):
    if arr[i][0] == 4 and arr[(i % 6 + 1) % 6][0] == 2 and arr[(i % 6 + 2) % 6][0] == 4:
        a, b = arr[(i % 6 + 1) % 6][1], arr[(i % 6 + 2) % 6][1]
        break
    elif arr[i][0] == 4 and arr[(i % 6 + 1) % 6][0] == 1 and arr[(i % 6 + 2) % 6][0] == 4:
        a, b = arr[i][1], arr[(i % 6 + 1) % 6][1]
        break
    elif arr[i][0] == 3 and arr[(i % 6 + 1) % 6][0] == 1 and arr[(i % 6 + 2) % 6][0] == 3:
        a, b = arr[(i % 6 + 1) % 6][1], arr[(i % 6 + 2) % 6][1]
        break
    elif arr[i][0] == 3 and arr[(i % 6 + 1) % 6][0] == 2 and arr[(i % 6 + 2) % 6][0] == 3:
        a, b = arr[i][1], arr[(i % 6 + 1) % 6][1]
        break

area = (max(sero) * max(garo)) - (a * b)

melon = T * area

print(melon)
