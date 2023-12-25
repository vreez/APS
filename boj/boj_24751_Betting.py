import sys; sys.stdin = open("24751.txt", "r")

a = int(input())
n = 100 / a
m = 100 / (100 - a)
print(n)
print(m)