import sys; sys.stdin = open("4998.txt", "r")

while True:
    try:
        n, m, b = map(float, input().split())
        y = 0
        while b > n:
            n += n * m / 100
            y += 1
        print(y)
    except:
        break