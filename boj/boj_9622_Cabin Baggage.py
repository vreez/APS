import sys; sys.stdin = open("9622.txt", "r")

T = int(input())
cnt = 0
for i in range(T):
    l, wi, d, we = map(float, input().split())
    if (l > 56 or wi > 45 or d > 25) and (l + wi + d > 125) or we > 7:
        print(0)
    else:
        print(1)
        cnt += 1
print(cnt)