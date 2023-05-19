import sys; sys.stdin = open("25756.txt", "r")

N = int(input())
arr = list(map(int, input().split()))
V = 0
for i in range(N):
    a = 1-(V/100)
    b = 1-(arr[i]/100)
    V = (1-(a*b))*100
    print(round(V, 6))