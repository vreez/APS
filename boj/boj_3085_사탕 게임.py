import sys; sys.stdin = open("input/3085.txt", "r")

N = int(input())
arr = [list(input()) for _ in range(N)]

def check(arr):
    maxNum = 0
    for i in range(len(arr)):
        count = 1
        for j in range(len(arr)-1):
            if arr[i][j] == arr[i][j+1]:
                count += 1
            else:
                count = 1
            if count > maxNum:
                maxNum = count

    for i in range(len(arr)):
        count = 1
        for j in range(len(arr)-1):
            if arr[j][i] == arr[j+1][i]:
                count += 1
            else:
                count = 1
            if count > maxNum:
                maxNum = count

    return maxNum

result = check(arr)
for i in range(N):
    for j in range(N-1):
        if arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            if result < check(arr):
                result = check(arr)
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if arr[j][i] != arr[j + 1][i]:
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]
            if result < check(arr):
                result = check(arr)
            arr[j][i], arr[j + 1][i] = arr[j + 1][i], arr[j][i]

print(result)

