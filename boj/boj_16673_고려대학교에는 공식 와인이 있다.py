import sys; sys.stdin = open("16673.txt", "r")

C, K, P = map(int, input().split())

total = 0
for i in range(1, C+1):
    total += ((K*i) + P*(i**2))

print(total)