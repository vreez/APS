import sys; sys.stdin = open("26768.txt", "r")

word = list(input())
for i in range(len(word)):
    if word[i] == 'a':
        word[i] = '4'
    elif word[i] == 'e':
        word[i] = '3'
    elif word[i] == 'i':
        word[i] = '1'
    elif word[i] == 'o':
        word[i] = '0'
    elif word[i] == 's':
        word[i] = '5'
print(''.join(word))