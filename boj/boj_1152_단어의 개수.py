import sys; sys.stdin = open("input/1152.txt", "r")

word = input()
if word == ' ':
    print(0)
else:
    word = word.strip()
    word = list(word.split(' '))
    print(len(word))