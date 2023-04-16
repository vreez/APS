import sys; sys.stdin = open("16483.txt", "r")

T = int(input())
answer = round((T/2)**2)
print(answer)