import sys; sys.stdin = open("10200.txt", "r")

T = int(input())
for tc in range(1, T+1):
    arr = list(map(int, input().split()))

    max_num = min_num = 0
    if arr[1] >= arr[2]:
        max_num = arr[1]
        min_num = arr[2]
    else:
        max_num = arr[2]
        min_num = arr[1]

    min_result = max_result = 0
    if arr[0] == max_num:
        min_result = min_num
    else:
        if arr[0] - max_num > min_num:
            min_result = 0
        else:
            min_result = min_num - (arr[0] - max_num)

    print("#{} {} {}".format(tc, min_num, min_result))