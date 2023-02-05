import sys; sys.stdin = open("4084.txt", "r")

while True:
    a, b, c, d = map(int, input().split())
    if a == b and b == c and c == d and a == 0:
        break
    else:
        cnt = 0
        while True:
            if a == b and b == c and c == d:
                break
            else:
                newA = abs(a-b)
                newB = abs(b-c)
                newC = abs(c-d)
                newD = abs(d-a)
                a = newA
                b = newB
                c = newC
                d = newD
                cnt += 1
    print(cnt)