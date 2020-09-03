import sys
sys.stdin = open("5097.txt")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = arr[M % N]


    print("#{} {}".format(tc, result))

