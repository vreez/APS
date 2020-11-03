import sys; sys.stdin = open("5209.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    my_arr = []
    total = 0
    nums = [i for i in range(N)]
    ans = 100000000000000
    def perm(k, total):
        global ans
        if total >= ans:
            return
        if k == N:
            if total < ans:
                ans = total
        else:
            for i in range(k, N):
                nums[k], nums[i] = nums[i], nums[k]
                perm(k + 1, total + arr[k][nums[k]])
                nums[k], nums[i] = nums[i], nums[k]

    perm(0, 0)
    print("#{} {}".format(tc, ans))