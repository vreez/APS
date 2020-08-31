import sys
sys.stdin = open("1204.txt")

T = int(input())
for tc in range(1, T+1):
    tc = int(input())
    arr = list(map(int, input().split()))

    count = [0] * 101

    for i in range(len(arr)):
        count[arr[i]] += 1
    # print(count)

    max_count = count[0]
    for j in range(len(count)):
        if count[j] >= max_count:
            max_count = count[j]
            idx = j

    print("#{} {}".format(tc, idx))