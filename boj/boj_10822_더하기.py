import sys; sys.stdin = open("10822.txt", "r")

S = list(map(int, input().split(",")))

total = 0
for i in range(len(S)):
    total += S[i]

print(total)