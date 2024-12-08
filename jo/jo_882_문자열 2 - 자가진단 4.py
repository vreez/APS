import sys; sys.stdin = open("882.txt", "r")

li = []
for _ in range(3):
    word = input()
    li.append(word)

new = sorted(li)

check = True
for i in range(3):
    if li[i] != new[i]:
        check = False
        break
if check == True:
    print("YES")
else:
    print("NO")
