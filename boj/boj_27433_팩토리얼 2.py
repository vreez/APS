import sys; sys.stdin = open("27433.txt", "r")

N = int(input())
answer = 1
for i in range(1, N+1):
    answer *= i

print(answer)    