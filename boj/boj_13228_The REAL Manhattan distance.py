import sys; sys.stdin = open("13228.txt", "r")

T = int(input())
for i in range(T):
    x1, y1, floor1, x2, y2, floor2 = map(int, input().split())
    answer = floor1 + abs(x2 - x1) + abs(y2 - y1) + floor2
    print(answer)