import sys; sys.stdin = open("11134.txt", "r")

T = int(input())
for i in range(T):
    N, C = map(int, input().split())
    answer = N // C
    if N % C:
        answer += 1
    print(answer)    