import sys; sys.stdin = open("1871.txt", "r")

N = int(input())
for _ in range(N):
    a, b = input().split("-")
    num = 0
    for i in range(len(a)):
        num += ((ord(a[i])-65) * (26**(len(a)-i-1)))
    if abs(num - int(b)) <= 100:
        print("nice")
    else:
        print("not nice")
