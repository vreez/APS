import sys; sys.stdin = open("11368.txt", "r")

while True:
    C, W, L, P = map(int, input().split())
    if C == W and W == L and L == P and C == 0:
        break
    else:
        ans = ((C**W)**L)**P
        print(ans)