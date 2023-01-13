import sys; sys.stdin = open("26500.txt", "r")

N = int(input())
for i in range(N):
    a, b = map(float, input().split())
    result = round(abs(a - b), 1)
    print(result)