import sys; sys.stdin = open("17487.txt", "r")

left = "qwertyasdfgzxcvb"
right = "uiophjklnm"
l, r, o = 0, 0, 0
word = input()
for i in range(len(word)):
    if word[i].isupper():
        o += 1
for i in range(len(word)):
    if word[i].lower() in left:
        l += 1
    elif word[i].lower() in right:
        r += 1
    else:
        o += 1

while o != 0:
    if l <= r:
        l += 1
        o -= 1
    else:
        r += 1
        o -= 1
print(l, r)