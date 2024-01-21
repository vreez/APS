import sys; sys.stdin = open("30979.txt", "r")

T = int(input())
N = int(input())
F = list(map(int, input().split()))
if sum(F) >= T:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")