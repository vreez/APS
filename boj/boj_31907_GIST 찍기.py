import sys; sys.stdin = open("31907.txt", "r")

K = int(input())
for i in range(3):
    for j in range(K):
        if i == 0:
            print("G"*K+"..."*K)
        elif i == 1:
            print("."*K+"I"*K+"."*K+"T"*K)
        else:
            print(".."*K+"S"*K+"."*K)
