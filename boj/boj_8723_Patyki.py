import sys; sys.stdin = open("8723.txt", "r")

a, b, c = map(int, input().split())

check1 = 0
check2 = 0

if a > b and a > c:
    hypo = a
    if a**2 == (b**2) + (c**2):
        check1 = 1
elif b > a and b > c:
    hypo = b
    if b**2 == (a**2) + (c**2):
        check1 = 1
elif c > a and c > b:
    hypo = c
    if c**2 == (a**2) + (b**2):
        check1 = 1
elif a == b and b == c:
    check2 = 1

if check1 == 0 and check2 == 0:
    print(0)
elif check1 == 1 and check2 == 0:
    print(1)
elif check1 == 0 and check2 == 1:
    print(2)



