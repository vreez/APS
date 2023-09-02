import sys; sys.stdin = open("1681.txt", "r")

N, L = map(int, input().split())
cnt = 0
num = 1
arr = []
while True:
    if cnt == N:
        break
    else:
        if str(L) not in str(num):
            cnt += 1
            arr.append(num)
        num += 1
print(arr[-1])
