import sys; sys.stdin = open("1032.txt", "r")

N = int(input())
arr = []
for i in range(N):
    words = list(input())
    arr.append(words)
l = len(arr[0])

new_arr = []
for i in range(l):
    temp = []
    for j in range(N):
        temp.append(arr[j][i])
    new_arr.append(temp)
answer = ''
for i in range(len(new_arr)):
    check = set(new_arr[i])
    check = list(check)
    if len(check) == 1:
        answer += check[0]
    else:
        answer += '?'

print(answer)
