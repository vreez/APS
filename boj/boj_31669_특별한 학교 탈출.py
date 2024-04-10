import sys; sys.stdin = open("31669.txt", "r")

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
check = 0
for i in range(M):
    flag = True
    for j in range(N):
        if arr[j][i] == "O":
            flag = False
            break
    if flag == True:
        check = i+1
        break
if check == 0:
    print("ESCAPE FAILED")
else:
    print(check)

