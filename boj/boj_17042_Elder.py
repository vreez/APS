import sys; sys.stdin = open("17042.txt", "r")

alpha = input()
N = int(input())
check = [alpha]

now = alpha
for i in range(N):
    z1, z2 = input().split()
    if z2 == now:
        if z1 not in check:
            check.append(z1)
        now = z1

print(now)
print(len(check))