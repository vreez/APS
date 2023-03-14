import sys; sys.stdin = open("2863.txt", "r")

a, b = map(int, input().split())
c, d = map(int, input().split())

total = []
total.append(a/c + b/d)
total.append(c/d + a/b)
total.append(d/b + c/a)
total.append(b/a + d/c)

big = -1
answer = -1

for i in range(4):
    if total[i] > big:
        big = total[i]
        answer = i
print(answer)