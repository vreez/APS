import sys; sys.stdin = open("21022.txt", "r")

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
score = 0
for i in range(N):
    if A[i] > B[i]:
        score += 3
    elif A[i] == B[i]:
        score += 1
print(score)
