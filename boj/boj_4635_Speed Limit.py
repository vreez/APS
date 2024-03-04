import sys; sys.stdin = open("4635.txt", "r")

while True:
    N = int(input())
    if N == -1:
        break
    else:
        time = 0
        total = 0
        for i in range(N):
            s, t = map(int, input().split())
            total += s * (t - time)
            time = t
        print("{} miles".format(total))
