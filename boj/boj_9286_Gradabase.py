import sys; sys.stdin = open("9286.txt", "r")

N = int(input())
for i in range(N):
    M = int(input())
    print("Case {}:".format(i+1))
    for j in range(M):
        num = int(input())
        if num < 6:
            print(num + 1)
            