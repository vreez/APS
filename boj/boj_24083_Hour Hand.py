import sys; sys.stdin = open("24083.txt", "r")

A = int(input())
B = int(input())

answer = A + (B % 12)
if answer > 12:
    answer = answer % 12
print(answer)