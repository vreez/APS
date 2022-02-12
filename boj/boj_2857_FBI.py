import sys; sys.stdin = open("2857.txt", "r")

answer = []

for i in range(5):
    name = input()
    if "FBI" in name:
        answer.append(i + 1)
if len(answer) > 0:
    for i in range(len(answer)):
        print(answer[i], end = " ")
else:
    print("HE GOT AWAY!")
