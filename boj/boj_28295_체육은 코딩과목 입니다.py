import sys; sys.stdin = open("28295.txt", "r")

direction = {1:'N', 2:'E', 3:'W', 4:'S'}
now = 'N'
for i in range(10):
    T = int(input())
    if now == 'N':
        if T == 1:
            now = 'E'
        elif T == 2:
            now = 'S'
        else:
            now = 'W'
    elif now == 'E':
        if T == 1:
            now = 'S'
        elif T == 2:
            now = 'W'
        else:
            now = 'N'
    elif now == 'W':
        if T == 1:
            now = 'N'
        elif T == 2:
            now = 'E'
        else:
            now = 'S'
    else:
        if T == 1:
            now = 'W'
        elif T == 2:
            now = 'N'
        else:
            now = 'E'

print(now)
