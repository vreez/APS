import sys; sys.stdin = open("3276.txt", "r")

N = int(input())
i = 1
j = 1
while True:
    if i * j >= N:
        break
    else:
        if i > j:
            j += 1
        else:
            i += 1
print(i, j)

