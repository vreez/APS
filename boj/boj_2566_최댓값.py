import sys; sys.stdin = open("2566.txt", "r")

arr = [list(map(int, input().split())) for _ in range(9)]
num = -1
a, b = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > num:
            a = i+1
            b = j+1
            num = arr[i][j]

print(num)
print(a, b)