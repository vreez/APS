import sys; sys.stdin = open("5717.txt", "r")

while True:
    M, F = map(int, input().split())
    if M == 0 and M == F:
        break
    else:
        print(M + F)