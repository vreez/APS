import sys; sys.stdin = open("11723.txt", "r")

M = int(sys.stdin.readline())
S = []

for _ in range(M):
    check = list(sys.stdin.readline().split())
    if check[0] == 'add':
        if int(check[1]) not in S:
            S.append(int(check[1]))
    elif check[0] == 'remove':
        if int(check[1]) in S:
            S.remove(int(check[1]))
    elif check[0] == 'check':
        if int(check[1]) in S:
            print(1)
        else:
            print(0)
    elif check[0] == 'toggle':
        if int(check[1]) in S:
            S.remove(int(check[1]))
        else:
            S.append(int(check[1]))
    elif check[0] == 'all':
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    elif check[0] == 'empty':
        S = []
