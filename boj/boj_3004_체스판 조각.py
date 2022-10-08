import sys; sys.stdin = open("3004.txt", "r")

N = int(input())

answer = 0
for i in range(N//2+1):
    result = (i+1) * (N-i+1)
    if result > answer:
        answer = result

print(answer)