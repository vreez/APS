arr = [
    [3, 5, 9],
    [2, 11, 5],
    [8, 30, 10],
    [22, 5, 1]
]
total = 0
for i in range(4):
    for j in range(3):
        print(arr[i][j], end=" ")
        total += arr[i][j]
    print()
print(total)
