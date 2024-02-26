import sys; sys.stdin = open("11131.txt", "r")

N = int(input())
for i in range(N):
    M = int(input())
    arr = list(map(int, input().split()))
    if sum(arr) < 0:
        print("Left")
    elif sum(arr) > 0:
        print("Right")
    else:
        print("Equilibrium")
