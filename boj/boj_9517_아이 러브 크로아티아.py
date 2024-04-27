import sys; sys.stdin = open("9517.txt", "r")

K = int(input())
N = int(input())
total = 0
for i in range(N):
    T, Z = input().split()
    total += int(T)
    if total >= 210:
        print(K)
        break
    else:
        if Z == "T":
            if K != 8:
                K += 1
            else:
                K = 1

