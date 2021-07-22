import sys; sys.stdin = open("input/1149.txt", "r")

N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    if i >= 1:
        house[i][0] = min(house[i-1][1], house[i-1][2]) + house[i][0]
        house[i][1] = min(house[i-1][0], house[i-1][2]) + house[i][1]
        house[i][2] = min(house[i-1][0], house[i-1][1]) + house[i][2]

print(min(house[N-1]))