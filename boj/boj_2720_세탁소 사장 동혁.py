import sys; sys.stdin = open("2720.txt", "r")

N = int(input())
for i in range(N):
    q = 0
    d = 0
    n = 0
    p = 0
    money = int(input())
    q = money // 25
    money -= 25 * q
    d = money // 10
    money -= 10 * d
    n = money // 5
    p = money % 5
    print(q, d, n, p)
