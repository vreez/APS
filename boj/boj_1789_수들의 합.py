import sys; sys.stdin = open("1789.txt", "r")

N = int(input())

i = 0
total = 0
for i in range(N):
    if total >= N:
        break
    else:
        i += 1
        total += i

if total > N:
    i -= 1

print(i)