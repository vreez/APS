import sys; sys.stdin = open("29267.txt", "r")

save = 0
bullet = 0

n, k = map(int, input().split())
for i in range(n):
    word = input()
    if word == "save":
        save = bullet
    elif word == "load":
        bullet = save
    elif word == "shoot":
        bullet -= 1
    else:
        bullet += k
    print(bullet)