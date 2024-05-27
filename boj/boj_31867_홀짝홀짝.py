import sys; sys.stdin = open("31867.txt", "r")

N = int(input())
odd = 0
even = 0
num = list(input())
for i in range(N):
    if int(num[i]) % 2 == 0:
        even += 1
    else:
        odd += 1
if odd > even:
    print(1)
elif even > odd:
    print(0)
else:
    print(-1)

