import sys; sys.stdin = open("10820.txt", "r")

while True:
    try:
        words = list(input())
        N = len(words)
        lower = 0
        upper = 0
        num = 0
        blank = 0
        for i in range(N):
            if words[i].islower() == True:
                lower += 1
            if words[i].isupper() == True:
                upper += 1
            if words[i].isdigit() == True:
                num += 1
            if words[i].isspace() == True:
                blank += 1

        print(lower, upper, num, blank)
    except EOFError:
        break