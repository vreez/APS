import sys; sys.stdin = open("28454.txt", "r")

now = list(map(int, input().split("-")))
N = int(input())
cnt = 0
for i in range(N):
    gift = list(map(int, input().split("-")))
    if gift[0] > now[0]:
        cnt += 1
    elif gift[0] == now[0]:
        if gift[1] > now[1]:
            cnt += 1
        elif gift[1] == now[1]:
            if gift[2] > now[2]:
                cnt += 1
            elif gift[2] == now[2]:
                cnt += 1
print(cnt)
