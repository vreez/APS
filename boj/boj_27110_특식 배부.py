import sys; sys.stdin = open("27110.txt", "r")

N = int(input())
A, B, C = map(int, input().split())

total = 0
if A < N:
    total += A
else:
    total += N

if B < N:
    total += B
else:
    total += N

if C < N:
    total += C
else:
    total += N

print(total)