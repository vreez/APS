import sys; sys.stdin = open("31495.txt", "r")

word = input()
flag = False
ans = ""
if len(word) > 2 and word[0] == '"' and word[-1] == '"':
    flag = True
else:
    flag = False
if flag == True:
    for i in range(1, len(word)-1):
        ans += word[i]
    print(ans)
else:
    print("CE")



