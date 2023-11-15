import sys; sys.stdin = open("15734.txt", "r")

L, R, A = map(int, input().split())
p1 = (L+A)
p2 = (R+A)
p3 = (L+R+A)//2
num = min(p1, p2, p3)
print(num*2)
