import sys; sys.stdin = open("2789.txt", "r")

word = ["C", "A", "M", "B", "R", "I", "D", "G", "E"]

N = list(input())

answer = ''
for i in range(len(N)):
    if N[i] not in word:
        answer += N[i]
print(answer)