import sys; sys.stdin = open("11795.txt", "r")

N = int(input())
total = [0, 0, 0]
for i in range(N):
    a, b, c = map(int, input().split())
    total[0] += a
    total[1] += b
    total[2] += c
    answer = min(total)
    if answer < 30:
        print("NO")
    else:
        total[0] -= answer
        total[1] -= answer
        total[2] -= answer
        print(answer)