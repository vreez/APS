import sys; sys.stdin = open("20352.txt", "r")

n = int(input())
pi = 3.14159265359
r = (n / pi) ** 0.5
answer = r * 2 * pi

print(answer)