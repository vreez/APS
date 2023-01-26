import sys; sys.stdin = open("26532.txt", "r")
import math

a, b = map(int, input().split())
answer = math.ceil(a * b / 4840 / 5)
print(answer)