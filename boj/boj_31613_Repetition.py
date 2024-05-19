import sys; sys.stdin = open("31613.txt", "r")

X = int(input())
N = int(input())
ans = 0
while True:
    if X >= N:
        break
    else:
        if X % 3 == 0:
            X += 1
        elif X % 3 == 1:
            X *= 2
        else:
            X *= 3
    ans += 1
print(ans)