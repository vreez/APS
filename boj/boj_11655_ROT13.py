import sys; sys.stdin = open("11655.txt", "r")

word = input()
small = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z'
    ]

large = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
    'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z'
    ]

for i in range(len(word)):
    for j in range(len(word[i])):
        if word[i][j] in small:
            inx = small.index(word[i][j])
            print(small[(inx + 13) % 26], end='')
        elif word[i][j] in large:
            inx = large.index(word[i][j])
            print(large[(inx + 13) % 26], end='')
        else:
            print(word[i][j], end='')


