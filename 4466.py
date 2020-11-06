import sys; sys.stdin = open("4466.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    result = 0

    my_list = sorted(arr, reverse=True)
    for i in range(K):
        result += my_list[i]

    print("#{} {}".format(tc, result))

