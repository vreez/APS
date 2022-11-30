import sys; sys.stdin = open("13528.txt", "r")

C = float(input())
L = int(input())
total = 0
for i in range(L):
    a, b = map(float, input().split())
    total += (a * b)
answer = C * total
print(format(answer, ".7f"))