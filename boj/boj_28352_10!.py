import sys; sys.stdin = open("28352.txt", "r")
import math

N = int(input())
result = math.factorial(N)

print(result // 60 // 60 // 24 // 7)

