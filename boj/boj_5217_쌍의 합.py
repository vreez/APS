import sys; sys.stdin = open("5217.txt", "r")

n = int(input())
for i in range(n):
    m = int(input())
    answer = []
    print("Pairs for {}:".format(m), end=" ")
    for j in range(1, m//2 + 1):
        if j != (m - j):
            if j != 1:
                print(",", end=" ")
            print(j, m-j, end="")
    print()