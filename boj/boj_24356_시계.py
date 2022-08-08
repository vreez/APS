import sys; sys.stdin = open("24356.txt", "r")

t1, m1, t2, m2 = map(int, input().split())
m1 += t1 * 60
m2 += t2 * 60
if m2 < m1:
    m2 += 24 * 60
m = m2 - m1
n = m // 30

print(m, n)