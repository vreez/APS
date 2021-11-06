import sys; sys.stdin = open("10987.txt", "r")

alpha = ['a', 'e', 'i', 'o', 'u']
word = list(input())
count = 0
for i in range(len(word)):
    if word[i] in alpha:
        count += 1

print(count)