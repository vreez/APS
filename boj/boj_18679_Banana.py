import sys; sys.stdin = open("18679.txt", "r")

N = int(input())
words = {}
for i in range(N):
    original, after = input().split(" = ")
    words[original] = after
total = int(input())
for i in range(total):
    count = int(input())
    sentence = list(input().split(" "))
    result = []
    for j in range(count):
        result.append(words[sentence[j]])

    for k in range(count):
        print(result[k], end=" ")
    print()
