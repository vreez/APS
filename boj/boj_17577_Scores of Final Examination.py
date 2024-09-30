import sys; sys.stdin = open("17577.txt", "r")

while True:
    n, m = map(int, input().split())
    if n == m and n == 0:
        break
    else:
        check = [0] * n
        for i in range(m):
            arr = list(map(int, input().split()))
            for j in range(n):
                check[j] += arr[j]

        print(max(check))
