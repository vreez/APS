import sys; sys.stdin = open("26004.txt", "r")

N = int(input())
arr = list(input())

cnt = [0, 0, 0, 0, 0]
E = 0
for i in range(N):
    if arr[i] == "H":
        cnt[0] += 1
    elif arr[i] == "I":
        cnt[1] += 1
    elif arr[i] == "A":
        cnt[2] += 1
    elif arr[i] == "R":
        cnt[3] += 1
    elif arr[i] == "C":
        cnt[4] += 1
    else:
        E += 1

if min(cnt) != 0:
    print(min(cnt))
else:
    print(0)