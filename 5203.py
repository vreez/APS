import sys; sys.stdin = open("5203.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    player1 = []
    player2 = []

    point1 = 0
    point2 = 0

    for i in range(12):
        if i % 2 == 0:
            if player1.count(arr[i]) == 2:
                point1 += 2
            elif arr[i] - 1 in player1 and arr[i] + 1 in player1:
                point1 += 2
            elif arr[i] - 2 in player1 and arr[i] - 1 in player1:
                point1 += 2
            elif arr[i] + 1 in player1 and arr[i] + 2 in player1:
                point1 += 2
            player1.append(arr[i])
            if point1 >= 2:
                print("#{} {}".format(tc, 1))
                break
        else:
            if player2.count(arr[i]) == 2:
                point2 += 2
            elif arr[i] - 1 in player2 and arr[i] + 1 in player2:
                point2 += 2
            elif arr[i] - 2 in player2 and arr[i] - 1 in player2:
                point2 += 2
            elif arr[i] + 1 in player2 and arr[i] + 2 in player2:
                point2 += 2
            player2.append(arr[i])
            if point2 >= 2:
                print("#{} {}".format(tc, 2))
                break
    if point1 < 2 and point2 < 2:
        print("#{} {}".format(tc, 0))
