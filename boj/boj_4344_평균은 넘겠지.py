import sys; sys.stdin = open("4344.txt", "r")

N = int(input())
for i in range(N):
    arr = list(map(int, input().split()))
    num = arr[0]
    new_arr = arr[1:]
    avg = sum(new_arr) // num

    cnt = 0
    for j in range(num):
        if new_arr[j] > avg:
            cnt += 1
    result = round(cnt / num * 100, 3)
    print("{:.3f}%".format(result))