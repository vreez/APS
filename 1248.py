import sys; sys.stdin = open('1248.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    V, E, A, B = map(int, input().split())
    arr = list(map(int, input().split()))

    L = [0] * (V+1)
    R = [0] * (V+1)
    P = [0] * (V+1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]
        P[c] = p
        if L[p] == 0:
            L[p] = c
        else:
            R[p] = c
    v = A
    A_list = []
    while v:
        A_list.append(v)
        v = P[v]

    v = B
    B_list = []
    while v:
        B_list.append(v)
        v = P[v]

    find_one = []
    for i in range(len(A_list)):
        for j in range(len(B_list)):
            if A_list[i] in B_list:
                find_one.append(A_list[i])

    ans = 0
    def traverse(v):
        global ans
        if v == 0: return
        traverse(L[v])
        traverse(R[v])
        ans += 1

    traverse(find_one[0])
    print('#{} {} {}'.format(tc, find_one[0], ans))


