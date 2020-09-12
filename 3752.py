import sys; sys.stdin = open('3752.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 중복 방지를 위해 리스트에 담긴 숫자의 합을 인덱스로 방문표시를 한다.
    visit = [0] * (sum(arr) + 1)
    Q = [0]
    for i in arr:
        for j in range(len(Q)):
            if visit[Q[j] + i]:  # 새롭게 계산된 값에 이미 방문 표시가 되어 있다면 건너 뛴다.
                continue
            else:
                visit[Q[j] + i] = 1 # 계산된 값에 방문표시가 되어 있지 않다면 방문표시를 한다.
                Q.append(Q[j] + i) # 계산된 값을 Q에 집어 넣는다.

    print('#{} {}'.format(tc, len(Q)))

