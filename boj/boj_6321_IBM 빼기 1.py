import sys; sys.stdin = open("6321.txt", "r")
alph_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
             'Y', 'Z']

N = int(input())
for i in range(N):
    word = list(input())
    answer = ''
    for j in range(len(word)):
        if word[j] == 'Z':
            answer += 'A'
        else:
            answer += alph_list[alph_list.index(word[j]) + 1]

    print("String #{}".format(i+1))
    print(answer)
    print()
