import sys; sys.stdin = open("2386.txt", "r")

while True:
    word = input()
    if word == '#':
        break
    else:
        words = list(word)
        alpha = words[0]
        count = 0
        for i in range(1, len(words)):
            if words[i].lower() == alpha:
                count += 1
        print(alpha, count)