import sys; sys.stdin = open("23971.txt", "r")
import math;

H, W, N, M = map(int, input().split())
first = math.ceil(H/(N+1))
second = math.ceil(W/(M+1))
print(first * second)