import sys; sys.stdin = open("2744.txt", "r")

word = list(input())

answer = ''

for i in range(len(word)):
    if word[i].islower() == True:
        answer += word[i].upper()
    else:
        answer += word[i].lower()

print(answer)