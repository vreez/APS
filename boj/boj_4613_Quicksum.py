import sys; sys.stdin = open("4613.txt", "r")

while True:
    word = list(input())
    if len(word) == 1 and word[0] == "#":
        break
    else:
        total = 0
        for i in range(len(word)):
            if word[i] != " ":
                total += ((i+1) * (ord(word[i])-64))
        print(total)
