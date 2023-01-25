import sys; sys.stdin = open("25881.txt", "r")

a, b = map(int, input().split())
n = int(input())
for i in range(n):
    use = int(input())
    if use <= 1000:
        price = use * a
    else:
        price = (1000 * a) + ((use - 1000) * b)

    print(use, price)