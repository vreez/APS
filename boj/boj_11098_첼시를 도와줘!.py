import sys; sys.stdin = open("11098.txt", "r")

tc = int(input())
for _ in range(tc):
    N = int(input())
    exp = 0
    player = ''
    for i in range(N):
        price, name = input().split(' ')
        if int(price) > exp:
            exp = int(price)
            player = name

    print(player)