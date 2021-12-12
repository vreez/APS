import sys; sys.stdin = open("1159.txt", "r")

words = {}

N = int(input())
for i in range(N):
    name = list(input())
    word = name[0]
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

answer = ''
for key, value in sorted(words.items()):
    if value >= 5:
        answer += key

if len(answer) > 0:
    print(answer)
else:
    print("PREDAJA")