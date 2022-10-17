import sys; sys.stdin = open("10178.txt", "r")

N = int(input())
for i in range(N):
    c, v = map(int, input().split())
    print("You get {} piece(s) and your dad gets {} piece(s).".format(c//v, c%v))