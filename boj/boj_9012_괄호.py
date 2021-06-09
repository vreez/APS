import sys; sys.stdin = open("9012.txt", "r")

N = int(input())
arr = [input() for _ in range(N)]

for i in range(N):
    keep = []
    flag = 'YES'
    for j in range(len(arr[i])):
        if j == len(arr[i])-1 and len(keep) > 1:
            flag = 'NO'
        elif arr[i][j] == '(':
            keep.append('(')
        elif arr[i][j] == ')' and len(keep) == 0:
            flag = 'NO'
            break
        elif arr[i][j] == ')' and len(keep) > 0:
            keep.pop()
    if len(keep) > 0:
        flag = 'NO'
    print(flag)

