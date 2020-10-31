import sys; sys.stdin = open("3499.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = input().split()
    new = [0] * N
    # 길이가 홀수일 경우와 짝수일 경우에 따라 중간지점을 다르게 설정해야 한다.
    if N % 2:
        mid = N // 2 + 1
    else:
        mid = N // 2

    for i in range(N):
        if i < mid:
            new[i * 2] = arr[i]
        else:
            new[(i - mid) * 2 + 1] = arr[i]

    print("#{}".format(tc), end=' ')
    for i in range(N):
        print(new[i], end=' ')
    print()

