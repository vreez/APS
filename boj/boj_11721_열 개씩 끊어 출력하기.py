import sys; sys.stdin = open("11721.txt", "r")

word = input()
len = len(word)

N = len // 10
if len % 10 > 0:
    N += 1

start = 0
for i in range(1, N + 1):
    end = 10 * i
    if i != N:
        print(word[start:end])
    else:
        print(word[start:])
    start = end