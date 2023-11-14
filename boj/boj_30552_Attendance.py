import sys; sys.stdin = open("30552.txt", "r")

N = int(input())
arr = []
name = []
for i in range(N):
    word = input()
    arr.append(word)
for i in range(1, N):
    if arr[i] == "Present!":
        arr[i-1] = 0
        arr[i] = 0
cnt = 0
for i in range(N):
    if arr[i] != 0:
        print(arr[i])
    else:
        cnt += 1
if cnt == N:
    print("No Absences")
