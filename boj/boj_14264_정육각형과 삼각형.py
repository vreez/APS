import sys; sys.stdin = open("14264.txt", "r")

N = int(input())

result = 3 ** 0.5 * N * N / 4

print(result)