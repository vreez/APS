import sys; sys.stdin = open("32025.txt", "r")

H = int(input()) * 100
W = int(input()) * 100
if H >= W:
    print(W//2)
else:
    print(H//2)



