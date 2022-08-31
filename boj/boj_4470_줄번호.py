import sys; sys.stdin = open("4470.txt", "r")

N = int(input())
for i in range(N):
    contents = input()
    print("{}. {}".format(i+1, contents))