import sys; sys.stdin = open("input/1929.txt", "r")
import math;

M, N = map(int, input().split())
arr = [True for i in range(N + 1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= N:
            arr[i * j] = False
            j += 1

for i in range(M, N + 1):
    if i > 1 and arr[i] == True:
        print(i)