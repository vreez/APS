import sys; sys.stdin = open('5178.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    H = [0] * (N+1)
    for _ in range(M):
        u, v = map(int, input().split())
        H[u] = v

    # 역으로 읽으면서 자식노드의 값을 부모노드에 차례로 더해준다.
    for i in range(N, 1, -1):
        H[i//2] += H[i]

    print('#{} {}'.format(tc, H[L]))