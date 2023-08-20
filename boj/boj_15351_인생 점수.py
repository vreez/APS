import sys; sys.stdin = open("15351.txt", "r")

N = int(input())
for i in range(N):
    word = list(input())
    total = 0
    for j in range(len(word)):
        if word[j] == " ":
            continue
        else:
            total += (ord(word[j])-64)
    if total == 100:
        print("PERFECT LIFE")
    else:
        print(total)