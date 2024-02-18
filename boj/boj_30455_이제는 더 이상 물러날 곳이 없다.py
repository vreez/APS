import sys; sys.stdin = open("30455.txt", "r")

N = int(input())
if N % 2 == 1:
    print("Goose")
else:
    print("Duck")