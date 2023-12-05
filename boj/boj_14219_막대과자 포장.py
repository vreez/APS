import sys; sys.stdin = open("14219.txt", "r")

n, m = map(int, input().split())

if n * m % 3 == 0:
    print("YES")
else:
    print("NO")