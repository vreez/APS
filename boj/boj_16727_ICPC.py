import sys; sys.stdin = open("16727.txt", "r")

#Persepolis
p1, s1 = map(int, input().split())
#Esteghlal
s2, p2 = map(int, input().split())

p = (p1 * 0.1) + p2
s = s1 + (s2 * 0.1)

if p > s:
    print("Persepolis")
elif s > p:
    print("Esteghlal")
else:
    print("Penalty")