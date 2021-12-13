import sys; sys.stdin = open("4458.txt", "r")

N = int(input())
for i in range(N):
    words = input().split()
    first = list(words[0])
    word = first[0].upper() + ''.join(first[1:])

    words[0] = word
    for i in range(len(words)):
        print(words[i], end=' ')
    print()