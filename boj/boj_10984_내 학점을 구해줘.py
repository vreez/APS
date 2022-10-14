import sys; sys.stdin = open("10984.txt", "r")

T = int(input())
for i in range(T):
    N = int(input())
    tot = 0
    avg = 0
    for j in range(N):
        C, G = map(float, input().split())
        tot += C
        avg += C*G
    print("{:.0f} {:.1f}".format(tot, avg/tot))
