import sys; sys.stdin = open("25904.txt", "r")

N, X = map(int, input().split())
arr = list(map(int, input().split()))
flag = True
check = X

while True:
    if flag == False:
        break
    for i in range(N):
        if arr[i] < check:
            flag = False
            answer = i+1
            break
        else:
            check += 1

print(answer)
