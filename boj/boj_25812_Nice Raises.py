import sys; sys.stdin = open("25812.txt", "r")

n, r = map(int, input().split())
one = 0
two = 0
for i in range(n):
    num = int(input())
    if num > r:
        two += 1
    elif num < r:
        one += 1
if one > two:
    print(1)
elif two > one:
    print(2)
else:
    print(0)