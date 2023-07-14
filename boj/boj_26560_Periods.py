import sys; sys.stdin = open("26560.txt", "r")

N = int(input())
for i in range(N):
    sen = input()
    new = list(sen)
    if new[-1] == ".":
        print(sen)
    else:
        print(sen+".")