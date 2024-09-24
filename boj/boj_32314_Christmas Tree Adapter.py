import sys; sys.stdin = open("32314.txt", "r")

a = int(input())
w, v = map(int, input().split())

if (w // v) >= a:
    print(1)
else:
    print(0)
