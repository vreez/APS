import sys; sys.stdin = open("5354.txt", "r")

N = int(input())
for _ in range(N):
    num = int(input())
    for i in range(num):
        for j in range(num):
            if i == 0 or i == (num-1) or j == 0 or j == (num-1):
                print("#", end="")
            else:
                print("J", end="")
        print()
    print()