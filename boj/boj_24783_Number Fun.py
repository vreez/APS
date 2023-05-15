import sys; sys.stdin = open("24783.txt", "r")

N = int(input())
for i in range(N):
    a, b, c = map(int, input().split())
    if a + b == c or a - b == c or b - a == c or a / b == c or b / a == c or a * b == c:
        print("Possible")
    else:
        print("Impossible")