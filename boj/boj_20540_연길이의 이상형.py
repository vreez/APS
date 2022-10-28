import sys; sys.stdin = open("20540.txt", "r")

N = list(input())
answer = ""

for i in range(4):
    if N[i] == "I":
        answer += "E"
    elif N[i] == "E":
        answer += "I"
    elif N[i] == "S":
        answer += "N"
    elif N[i] == "N":
        answer += "S"
    elif N[i] == "T":
        answer += "F"
    elif N[i] == "F":
        answer += "T"
    elif N[i] == "J":
        answer += "P"
    else:
        answer += "J"

print(answer)
