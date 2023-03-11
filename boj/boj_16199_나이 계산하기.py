import  sys; sys.stdin = open("16199.txt", "r")

birth = list(map(int, input().split()))
day = list(map(int, input().split()))

a = 0
b = day[0] - birth[0] + 1
c = day[0] - birth[0]
if day[0] == birth[0]:
    a = day[0] - birth[0]
elif day[0] > birth[0]:
    if day[1] > birth[1]:
        a = day[0] - birth[0]
    elif day[1] == birth[1]:
        if day[2] < birth[2]:
            a = day[0] - birth[0] - 1
        elif day[2] >= birth[2]:
            a = day[0] - birth[0]
    else:
        a = day[0] - birth[0] - 1

print(a)
print(b)
print(c)


