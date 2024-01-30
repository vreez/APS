import sys; sys.stdin = open("27245.txt", "r")

w = int(input())
l = int(input())
h = int(input())

mi = min(w, l)
mx = max(w, l)

if (mi / h) >= 2 and (mx / mi) <= 2:
    print("good")
else:
    print("bad")




