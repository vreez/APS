import sys; sys.stdin = open("31712.txt", "r")

yc, yd = map(int, input().split())
dc, dd = map(int, input().split())
pc, pd = map(int, input().split())
H = int(input())
time = 0
H = H - (yd + dd + pd)
while True:
    if H <= 0:
        break
    else:
        time += 1
        if time >= yc and time % yc == 0:
            H -= yd
        if time >= dc and time % dc == 0:
            H -= dd
        if time >= pc and time % pc == 0:
            H -= pd

print(time)