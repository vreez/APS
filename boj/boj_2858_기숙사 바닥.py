import sys; sys.stdin = open("2858.txt", "r")

R, B = map(int, input().split())
LplustW = (R + 4) // 2
LW = R + B

for i in range(1, LplustW):
    if (LplustW - i) * i == LW:
        if LplustW-i >= i:
            print(LplustW-i, end=" ")
            print(i)
