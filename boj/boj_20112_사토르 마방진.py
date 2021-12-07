import sys; sys.stdin = open("20112.txt", "r")

N = int(input())
arr = []
for i in range(N):
    arr.append(list(input()))

flag = True
for i in range(N):
    check = []
    for j in range(N):
        check.append(arr[j][i])
    if check != arr[i]:
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')