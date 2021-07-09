import sys; sys.stdin = open("input/1316.txt", "r")

N = int(input())
arr = list(input() for _ in range(N))

count = 0
for i in range(N):
    over = []
    for j in range(len(arr[i])):
        flag = True
        if arr[i][j] in over:
            flag = False
            break
        if j < len(arr[i]) - 1:
            if arr[i][j] != arr[i][j+1]:
                over.append(arr[i][j])
    if flag == True:
        count += 1

print(count)