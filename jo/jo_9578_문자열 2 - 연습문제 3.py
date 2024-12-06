import sys; sys.stdin = open("9578.txt", "r")

word = input()
for i in range(len(word)):
    print(word[i+1:] + word[:i+1])