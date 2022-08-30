import sys; sys.stdin = open("25314.txt", "r")

N = int(input())
answer = ""
for i in range(N//4):
    answer += "long "

answer += "int"

print(answer)