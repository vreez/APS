import sys; sys.stdin = open("8710.txt", "r")

k, w, m = map(int, input().split())

result = (w - k) // m
if (w - k) % m > 0:
    result += 1

print(result)

