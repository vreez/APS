import sys; sys.stdin = open("13610.txt", "r")

x, y = map(int, input().split())
n = 1
while True:
    if y*n - x*n >= y:
        break
    n += 1
print(n)