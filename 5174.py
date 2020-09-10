# 후위순회를 해야 한다.

import sys;sys.stdin = open('5174.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    temp = list(map(int, input().split()))

    L = [0] * (E+2)
    R = [0] * (E+2)
    P = [0] * (E+2)

    for i in range(0, E*2, 2):
        u, v = temp[i], temp[i+1]
        if L[u] == 0:
            L[u] = v
        else:
            R[u] = v
        P[v] = u

    cnt = 0
    def postorder(v):
        global cnt
        if v == 0:
            return 0
        cnt += 1
        l = postorder(L[v])
        r = postorder(R[v])
        return l + r + 1

    print('#{} {}'.format(tc, postorder(N)))
