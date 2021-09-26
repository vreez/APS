import sys; sys.stdin = open("1100.txt", "r")

arr = [list(input()) for _ in range(8)]
standard = [['B'] * 8 for _ in range(8)]

for i in range(8):
    for j in range(8):
        if i % 2 == 0:
            if j % 2 == 0:
                standard[i][j] = 'W'
        else:
            if j % 2 != 0:
                standard[i][j] = 'W'

count = 0
for i in range(8):
    for j in range(8):
        if arr[i][j] == 'F':
            if standard[i][j] == 'W':
                count += 1

print(count)