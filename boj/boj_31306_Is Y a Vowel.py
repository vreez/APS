import sys; sys.stdin = open("31306.txt", "r")

word = list(input())
vowel = ['a', 'e', 'i', 'o', 'u']
cntV = 0
cntY = 0
for i in range(len(word)):
    if word[i] in vowel:
        cntV += 1
    if word[i] == "y":
        cntY += 1
print(cntV, cntY+cntV)