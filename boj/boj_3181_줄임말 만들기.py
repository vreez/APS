import sys; sys.stdin = open("3181.txt", "r")

check = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
word = list(input().split())
new = ""
for i in range(len(word)):
    if i == 0 or word[i] not in check:
        new += word[i][0].upper()

print(new)
