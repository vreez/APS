import sys; sys.stdin = open("2292.txt", "r")

N = int(input())
num = 1
for i in range(N):
    num += (6*i)
    if N <= num:
        print(i+1)
        break