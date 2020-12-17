n, m = map(int, input().split())

while 0 > n or n > 100 or 1 > m or m > 3:
    print('INPUT ERROR!')
    n, m = map(int, input().split())

if m == 1:
    a = 1
    b = 0
    for i in range(n):
        for j in range(a+b):
            print('*', end='')
        print()
        b += 1

elif m == 2:
    a = 0
    for i in range(n):
        for j in range(n-a):
            print('*', end='')
        print()
        a += 1

else:
    arr = [[0] * (n * 2 - 1) for _ in range(n)]
    a = 0
    for i in range(n):
        for j in range(n-1-a, n+a):
            arr[i][j] = '*'
        a += 1

    for i in range(n):
        for j in range(n * 2 - 1):
            if arr[i][j] == '*':
                print(arr[i][j], end='')
            else:
                print(' ', end='')
        print()



