import sys; sys.stdin = open("5292.txt", "r")

N = int(input())
for i in range(1, N+1):
    if i % 3 == 0 and i % 5 == 0:
        print("DeadMan")
    elif i % 3 == 0:
        print("Dead")
    elif i % 5 == 0:
        print("Man")
    else:
        print(i, end=" ")