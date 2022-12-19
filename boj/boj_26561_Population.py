import sys; sys.stdin = open("26561.txt", "r")

N = int(input())
for i in range(N):
    p, t = map(int, input().split())
    answer = p - (t // 7) + (t // 4)
    print(answer)