import sys; sys.stdin = open("3059.txt", "r")

N = int(input())
for i in range(N):
    word = list(input())
    check = []
    total = 0
    for j in range(len(word)):
        if word[j] not in check:
            check.append(word[j])
            total += ord(word[j])
    print(2015-total)