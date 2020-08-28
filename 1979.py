import sys
sys.stdin = open("1979.txt")

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for j in range(N):
        stack = []
        for i in range(N):
            if (i == N - 1 and arr[j][i] == 1 and len(stack) == M - 1) or (len(stack) == M and arr[j][i] == 0):
                cnt += 1
                stack = []
            elif len(stack) != M and len(stack) > 0 and arr[j][i] == 0:
                stack = []
            elif arr[j][i] == 1:
                stack.append(1)

    i = j = 0
    for j in range(N):
        stack = []
        for i in range(N):
            if (i == len(arr) - 1 and arr[i][j] == 1 and len(stack) == M - 1) or (len(stack) == M and arr[i][j] == 0):
                cnt += 1
                stack = []
            elif len(stack) != M and len(stack) > 0 and arr[i][j] == 0:
                stack = []
            elif arr[i][j] == 1:
                stack.append(1)
    print('#{} {}'.format(t, cnt))

