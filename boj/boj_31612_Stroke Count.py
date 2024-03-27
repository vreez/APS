import sys; sys.stdin = open("31612.txt", "r")

N = int(input())
S = list(input())
total = 0

for i in range(N):
    if S[i] == "j":
        total += 2
    elif S[i] == "o":
        total += 1
    else:
        total += 2
print(total)