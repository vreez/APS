import sys; sys.stdin = open("2875.txt", "r")

N, M, K = map(int, input().split())
team = 0
while True:
    if N >= 2 and M >= 1 and N + M - 3 >= K:
        N -= 2
        M -= 1
        team += 1
    else:
        break
print(team)