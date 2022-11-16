import sys; sys.stdin = open("13225.txt", "r")

N = int(input())
for i in range(N):
    num = int(input())
    cnt = 0
    for j in range(1, num+1):
        if num % j == 0:
            cnt += 1
    print(num, cnt)