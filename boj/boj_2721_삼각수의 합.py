import sys; sys.stdin = open("2721.txt", "r")

N = int(input())
for i in range(N):
    num = int(input())
    total = 0
    for j in range(1, num+1):
        total += (j * (((j+1) * (j+2))//2))
    print(total)