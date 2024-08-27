import sys; sys.stdin = open("16171.txt", "r")

word = list(input())
keyword = input()
ans = ""
for i in word:
    if i.isalpha() == True:
        ans += i
if keyword in ans:
    print(1)
else:
    print(0)