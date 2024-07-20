import sys; sys.stdin = open("30700.txt", "r")

word = list(input())
korea = ["K", "O", "R", "E", "A"]
a = 0
check = 0
for i in range(len(word)):
    if word[i] == korea[a]:
        check += 1
        a += 1
    if a == 5:
        a = 0
print(check)

