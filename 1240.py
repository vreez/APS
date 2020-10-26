import sys; sys.stdin = open("1240.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    my_arr = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if arr[i][j] == 1:
                my_arr.append(arr[i][j-55:j+1])
                break

    new_list = [0] * 8
    for k in range(0, 56, 7):
        if my_arr[0][k:k+7] == [0, 0, 0, 1, 1, 0, 1]:
            new_list[k//7] = 0
        elif my_arr[0][k:k+7] == [0, 0, 1, 1, 0, 0, 1]:
            new_list[k//7] = 1
        elif my_arr[0][k:k+7] == [0, 0, 1, 0, 0, 1, 1]:
            new_list[k//7] = 2
        elif my_arr[0][k:k+7] == [0, 1, 1, 1, 1, 0, 1]:
            new_list[k//7] = 3
        elif my_arr[0][k:k+7] == [0, 1, 0, 0, 0, 1, 1]:
            new_list[k//7] = 4
        elif my_arr[0][k:k+7] == [0, 1, 1, 0, 0, 0, 1]:
            new_list[k//7] = 5
        elif my_arr[0][k:k+7] == [0, 1, 0, 1, 1, 1, 1]:
            new_list[k//7] = 6
        elif my_arr[0][k:k+7] == [0, 1, 1, 1, 0, 1, 1]:
            new_list[k//7] = 7
        elif my_arr[0][k:k+7] == [0, 1, 1, 0, 1, 1, 1]:
            new_list[k//7] = 8
        elif my_arr[0][k:k+7] == [0, 0, 0, 1, 0, 1, 1]:
            new_list[k//7] = 9

    odd = 0
    even = 0
    for i in range(8):
        if i % 2 == 0:
            odd += new_list[i]
        else:
            even += new_list[i]

    if (odd * 3 + even) % 10 == 0:
        print("#{} {}".format(tc, (odd+even)))
    else:
        print("#{} {}".format(tc, 0))
