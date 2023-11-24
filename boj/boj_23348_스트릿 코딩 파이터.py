import sys; sys.stdin = open("23348.txt", "r")

A, B, C = map(int, input().split())
N = int(input())
score = []
for i in range(N):
    total = 0
    for j in range(3):
        one, two, three = map(int, input().split())
        total += ((one * A) + (two * B) + (three * C))
    score.append(total)

print(max(score))