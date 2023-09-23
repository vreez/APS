import sys; sys.stdin = open("28701.txt", "r")

N = int(input())
a = 0
b = 0
for i in range(1, N+1):
    a += i
    b += (i**3)
print(a)
print(a**2)
print(b)