import sys; sys.stdin = open("27918.txt", "r")

N = int(input())
X = 0
Y = 0
for i in range(N):
    w = input()
    if w == 'D':
        X += 1
    else:
        Y += 1
    if abs(X-Y) >= 2:
        break
print("{}:{}".format(X, Y))