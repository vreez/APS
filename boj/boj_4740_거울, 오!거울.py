import sys; sys.stdin = open("4740.txt", "r")

while True:
    word = input()
    if word == "***":
        break
    else:
        answer = word[::-1]
        print(answer)
            