import sys; sys.stdin = open("31994.txt", "r")

check = 0
ans = ""
for i in range(7):
    name, num = input().split()
    if check < int(num):
        check = int(num)
        ans = name
print(ans)

