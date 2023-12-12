import sys; sys.stdin = open("30822.txt", "r")

N = int(input())
arr = list(input())

u = arr.count("u")
o = arr.count("o")
s = arr.count("s")
p = arr.count("p")
c = arr.count("c")

new = [u, o, s, p, c]

print(min(new))