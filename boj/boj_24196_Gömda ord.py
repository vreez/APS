import sys; sys.stdin = open("24196.txt", "r")

word = list(input())
num = 0
answer = ""
while True:
    if num >= len(word):
        break
    else:
        answer += word[num]
        num += ord(word[num]) - 64

print(answer)