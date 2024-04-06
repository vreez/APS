import sys; sys.stdin = open("31520.txt", "r")

num = input()
flag = True

for i in range(len(num)):
    if int(num[i]) != i + 1:
        print(-1)
        flag = False
        break
if flag == True:
    print(num[-1])
