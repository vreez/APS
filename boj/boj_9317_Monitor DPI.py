import sys; sys.stdin = open("9317.txt", "r")

while True:
    D, RH, RV = map(float, input().split())
    if D == RH and RH == RV and D == 0:
        break
    else:
        W = 16 * D / (337**(1/2))
        H = 9 / 16 * W
        print("Horizontal DPI: {:.2f}".format(RH/W))
        print("Vertical DPI: {:.2f}".format(RV/H))