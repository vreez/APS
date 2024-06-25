import sys; sys.stdin = open("5026.txt", "r")

N = int(input())
for i in range(N):
    word = input()
    if word[0] == "P":
        print("skipped")
    else:
        a, b = map(int, word.split("+"))
        print(a + b)