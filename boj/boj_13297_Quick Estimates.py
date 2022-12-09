import sys; sys.stdin = open("13297.txt", "r")

N = int(input())
for i in range(N):
    num = list(input())
    print(len(num))