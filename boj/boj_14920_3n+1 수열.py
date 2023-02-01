import sys; sys.stdin = open("14920.txt", "r")

N = int(input())
cnt = 1
while True:
    if N == 1:
        break
    else:
        if N % 2 == 0:
            N = N // 2
        else:
            N = (3 * N) + 1
        cnt += 1

print(cnt)
