import sys; sys.stdin = open("2902.txt", "r")

words = list(input().split('-'))
answer = ''
for i in range(len(words)):
    answer += words[i][0]
print(answer)