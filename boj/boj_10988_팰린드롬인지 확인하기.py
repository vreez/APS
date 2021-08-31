import sys; sys.stdin = open("10988.txt", "r")

word = list(input())
answer = 1
for i in range(len(word) // 2):
    if word[i] == word[len(word) - 1 - i]:
        continue
    else:
        answer = 0
print(answer)