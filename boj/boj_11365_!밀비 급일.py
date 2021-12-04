import sys; sys.stdin = open("11365.txt", "r")

while True:
    sen = input()
    if sen == 'END':
        break
    else:
        words = list(reversed(sen))
        print(''.join(words))