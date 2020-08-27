import copy
import sys
sys.stdin = open("1211.txt")


for t in range(1, 11):
    t = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    m = []
    for i in range(100):
        if arr[0][i] == 1:
            m.append((i))

    my_dict = {}

    for j in m:
        copy_arr = copy.deepcopy(arr)
        n = 0
        cnt = 1
        k = j
        my_dict[k] = 0
        while n != 99:
            if (copy_arr[n][j] == 3 or copy_arr[n - 1][j] == 3) and j > 0 and copy_arr[n][j - 1] == 1:
                j -= 1
                cnt += 1
                copy_arr[n][j] = 3
            elif (copy_arr[n][j] == 3 or copy_arr[n - 1][j] == 3) and j < 99 and copy_arr[n][j + 1] == 1:
                j += 1
                cnt += 1
                copy_arr[n][j] = 3
            else:
                n += 1
                cnt += 1
                copy_arr[n][j] = 3

        my_dict[k] = cnt

    for idx, count in my_dict.items():
        if count == min(my_dict.values()):
            print("#{} {}".format(t, idx))