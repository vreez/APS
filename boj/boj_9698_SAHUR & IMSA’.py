import sys; sys.stdin = open("9698.txt", "r")

T = int(input())
for i in range(T):
    H, M = map(int, input().split())
    if M >= 45:
        M -= 45
    else:
        M = M + 60 - 45
        if H == 0:
            H = 23
        else:
            H -= 1
    print("Case #{}: {} {}".format(i+1, H, M))


