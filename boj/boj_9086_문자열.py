import sys; sys.stdin = open("9086.txt", "r")

N = int(input())
for i in range(N):
    word = list(input())
    print(word[0] + word[-1])