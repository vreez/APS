import sys; sys.stdin = open("1974.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    total = 0
    # 행 검증
    check = 0
    for i in range(9):
        my_list = []
        for j in range(9):
            my_list.append(arr[i][j])
        new_list = set(my_list)
        if len(new_list) == 9:
            check += 1

    if check == 9:
        total += 1

    # 열 검증
    check = 0
    for i in range(9):
        my_list = []
        for j in range(9):
            my_list.append(arr[j][i])
        new_list = set(my_list)
        if len(new_list) == 9:
            check += 1

    if check == 9:
        total += 1

    # 박스 검증
    check = 0
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            my_list = []
            for n in range(i+3):
                for m in range(j+3):
                    my_list.append(arr[n][m])

            new_list = set(my_list)
            if len(new_list) == 9:
                check += 1

    if check == 9:
        total += 1

    if total == 3:
        print("#{} {}".format(tc, 1))
    else:
        print("#{} {}".format(tc, 0))

