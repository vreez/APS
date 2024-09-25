import sys; sys.stdin = open("32326.txt", "r")
R = int(input())
G = int(input())
B = int(input())

ans = (R * 3) + (G * 4) + (B * 5)
print(ans)