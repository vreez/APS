import sys; sys.stdin = open("11656.txt", "r")

word = list(input())
words = []
for i in range(len(word)):
    words.append(''.join(word[i:]))
words.sort()
for i in range(len(words)):
    print(words[i])