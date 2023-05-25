import sys; sys.stdin = open("6750.txt", "r")

word = list(input())
alpha = ["I", "O", "S", "H", "Z", "X", "N"]
check = True
for i in range(len(word)):
    if word[i] not in alpha:
        check = False
        break

if check == True:
    print("YES")
else:
    print("NO")