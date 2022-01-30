import sys; sys.stdin = open("2525.txt", "r")

A, B = map(int, input().split())
C = int(input())

H = C // 60 + A
M = C % 60 + B

if M >= 60:
    M -= 60
    H += 1

if H >= 24:
    H -= 24

print(H, M)