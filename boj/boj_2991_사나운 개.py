import sys; sys.stdin = open("2991.txt", "r")

A, B, C, D = map(int, input().split())
arr = list(map(int, input().split()))

for i in arr:
    answer = 0
    if 0 < i % (A+B) and i % (A+B) <= A:
        answer += 1
    if 0 < i % (C+D) and i % (C+D) <= C:
        answer += 1

    print(answer)