import sys; sys.stdin = open("25191.txt", "r")

N = int(input())
A, B = map(int, input().split())

answer = min(N, (A // 2) + B)

print(answer)