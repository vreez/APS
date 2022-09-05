import sys; sys.stdin = open("14065.txt", "r")

N = float(input())
result = 100.00 / (1.609344 / 3.785411784 * N)
print(round(result, 6))