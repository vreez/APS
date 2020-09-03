import sys
sys.stdin = open("4881.txt")

def dfs(row, sum):
    global min_sum
    if row == N:
        if sum <= min_sum:
            min_sum = sum
        return min_sum

    if sum > min_sum:
        return

    else:
        for col in range(N):
            if visit[col] == 0:
                if arr[row][col]:
                    visit[col] = 1
                    dfs(row+1, sum + arr[row][col])
                    visit[col] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * N
    min_sum = 101

    dfs(0, 0)

    print("#{} {}".format(tc, min_sum))



