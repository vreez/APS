import sys
sys.stdin = open("1959.txt")

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    Aj = list(map(int, input().split()))
    Bj = list(map(int, input().split()))

    if N > M:
        Aj, Bj = Bj, Aj

    A = len(Aj)
    B = len(Bj)
    s = 0
    e = s + A

    total = []
    while s < B - A + 1:
        count = 0
        for i in range(A):
            new_Bj = Bj[s:e]
            count += new_Bj[i] * Aj[i]
        s += 1
        e += 1
        total.append(count)

    max_num = total[0]
    for t in total:
        if t >= max_num:
            max_num = t

    print("#{} {}".format(tc, max_num))

