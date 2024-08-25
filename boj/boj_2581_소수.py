import sys; sys.stdin = open("2581.txt", "r")

M = int(input())
N = int(input())
arr = []
for i in range(M, N+1):
    check = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                check += 1
                break
        if check == 0:
            arr.append(i)
if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)