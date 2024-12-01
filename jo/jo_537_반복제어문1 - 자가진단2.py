import sys; sys.stdin = open("537.txt", "r")

num = int(input())
n = 1
total = 0
while True:
    if n > num:
        break
    else:
        total += n
        n += 1
print(total)