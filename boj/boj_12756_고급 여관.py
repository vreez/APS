import sys; sys.stdin = open("12756.txt", "r")

a1, l1 = map(int, input().split())
a2, l2 = map(int, input().split())

while True:
    c1 = l1 - a2
    c2 = l2 - a1
    if c1 <= 0 or c2 <= 0:
        break
    else:
        l1 = c1
        l2 = c2

if c1 <= 0:
    if c2 <= 0:
        print("DRAW")
    else:
        print("PLAYER B")
if c2 <= 0:
    if c1 > 0:
        print("PLAYER A")