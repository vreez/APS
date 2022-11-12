import sys; sys.stdin = open("10865.txt", "r")

N, M = map(int, input().split())
friends = [0] * (N + 1)
for i in range(M):
    A, B = map(int, input().split())
    friends[A] += 1
    friends[B] += 1
for i in range(1, N+1):
    print(friends[i])
