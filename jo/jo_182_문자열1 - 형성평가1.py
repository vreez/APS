import sys; sys.stdin = open("182.txt", "r")

a, b = input().split()
pl = ord(a) + ord(b)
mi = abs(ord(a) - ord(b))
print(pl, mi)