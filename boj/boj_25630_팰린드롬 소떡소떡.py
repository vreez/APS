import sys; sys.stdin = open("25630.txt", "r")

N = int(input())
word = list(input())
answer = 0
for i in range(N//2):
    if word[i] != word[N-1-i]:
        answer += 1

print(answer)