import sys; sys.stdin = open("4564.txt", "r")

while True:
    N = input()
    if N == "0":
        break
    else:
        while int(N) // 10 > 0:
            total = 1
            print(N, end=" ")
            for a in N:
                total *= int(a)
            N = str(total)
        print(N)