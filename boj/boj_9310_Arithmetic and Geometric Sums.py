import sys; sys.stdin = open("9310.txt", "r")

while True:
    N = int(input())
    if N == 0:
        break
    else:
        a, b, c = map(int, input().split())
        if b - a == c - b:
            d = b - a
            ans = N * (2*a + (N-1)*d) // 2
        else:
            r = b // a
            ans = a * (((r**N)-1) // (r-1))
        print(ans)