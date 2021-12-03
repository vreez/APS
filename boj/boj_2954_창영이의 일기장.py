import sys; sys.stdin = open("2954.txt", "r")

vowel = ['a', 'e', 'i', 'o', 'u']

diary = list(input().split())
result = []
for i in range(len(diary)):
    words = list(diary[i])
    for j in range(len(words)):
        if j != 0 and words[j] == 'p' and words[j-1] in vowel and words[j+1] in vowel and words[j-1] == words[j+1]:
            words[j] = ''
            words[j+1] = ''
    words = ''.join(words)
    result.append(words)

for i in range(len(result)):
    print(result[i], end=" ")

