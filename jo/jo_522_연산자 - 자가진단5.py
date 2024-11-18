import sys; sys.stdin = open("522.txt", "r")

a, b = map(int, input().split())
if a == b:
    print(1)
else:
    print(0)
if a != b:
    print(1)
else:
    print(0)