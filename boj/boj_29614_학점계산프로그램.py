import sys; sys.stdin = open("29614.txt", "r")

grade = {
    "A+":4.5, "A":4.0, "B+":3.5, "B":3.0, "C+":2.5, "C":2.0,
    "D+":1.5, "D":1.0, "F":0.0
}

score = list(input())
new = []
for i in range(len(score)):
    if score[i] != "+":
        new.append(score[i])
    else:
        new[-1] += "+"
total = 0
for g in new:
    total += grade[g]
ans = total / len(new)
print(ans)

