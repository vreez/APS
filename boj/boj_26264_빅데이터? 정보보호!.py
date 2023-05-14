import sys; sys.stdin = open("26264.txt", "r")

N = int(input())
words = list(input())
b = 0
s = 0
i = 0
for _ in range(N):
    if words[i] == "s":
        s += 1
        i += 8
    else:
        b += 1
        i += 7

if s > b:
    print("security!")
elif b > s:
    print("bigdata?")
else:
    print("bigdata? security!")
