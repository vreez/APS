import sys; sys.stdin = open("24294.txt", "r")

w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())
total = 4
total += ((h1 + h2) * 2)
if w1 >= w2:
    total += (w1 * 2)
else:
    total += (w2 * 2)

print(total)