import sys; sys.stdin = open("input/9251.txt", "r")

word1 = [0] + list(input())
word2 = [0] + list(input())

arr = [[0] * len(word2) for _ in range(len(word1))]

for i in range(1, len(word1)):
    for j in range(1, len(word2)):
        if word1[i] == word2[j]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])


print(arr[len(word1)-1][len(word2)-1])


