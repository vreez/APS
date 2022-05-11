import sys; sys.stdin = open("14924.txt", "r")

S, T, D = map(int, input().split())

result = D // (S * 2) * T

print(result)