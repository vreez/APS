import sys; sys.stdin = open("1859.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sell = list(map(int, input().split()))

    target = sell[-1]
    total = 0
    for i in range(N-2, -1, -1):
        if sell[i] <= target:
            total += (target-sell[i])
        elif sell[i] > target:
            target = sell[i]

    print("#{} {}".format(tc, total))

