import sys; sys.stdin = open("5013.txt", "r")

N = int(input())
answer = 0
for i in range(N):
    flag = True
    arr = list(input())
    for j in range(1, len(arr)):
        if arr[j-1] == "C" and arr[j] == "D":
            flag = False
            break
    if flag == True:
        answer += 1

print(answer)