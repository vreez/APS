# 모든 부분 집합을 생성하여 푸는 문제
import sys; sys.stdin = open("5215.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(1<<N): # 0부터 2^N-1까지 총 2^N번의 경우가 존재한다.
        score = 0
        calo = 0
        for j in range(N):
            if i & (1<<j): # i의 j번째 요소가 1인지 아닌지를 판단한다.
                score += arr[j][0]
                calo += arr[j][1]
        if calo <= L:  # 정해진 칼로리보다 낮은 경우에만 판단한다.
            ans = max(score, ans)

    print("#{} {}".format(tc, ans))