import sys; sys.stdin = open("19698.txt", "r")

N, W, H, L = map(int, input().split())

result = (H // L) * (W // L)

print(min(result, N))