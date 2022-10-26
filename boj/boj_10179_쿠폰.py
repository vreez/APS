import sys; sys.stdin = open("10179.txt", "r")

N = int(input())
for i in range(N):
    num = float(input())
    dc = num * 0.8
    print("${:.2f}".format(dc))