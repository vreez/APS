import sys; sys.stdin = open("10798.txt", "r")

arr = [list(input()) for _ in range(5)]

max_len = 0
for i in range(5):
    if len(arr[i]) > max_len:
        max_len = len(arr[i])

new_arr = [[0] * max_len for _ in range(5)]

for i in range(5):
    for j in range(max_len):
        if j >= len(arr[i]):
            new_arr[i][j] = '*'
        else:
            new_arr[i][j] = arr[i][j]

for j in range(max_len):
    for i in range(5):
        if new_arr[i][j] == '*':
            print('', end='')
        else:
            print(new_arr[i][j], end='')
