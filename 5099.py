import sys; sys.stdin = open('5099.txt', 'r')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheeze = list(map(int, input().split()))
    Q = []
    # 피자번호를 Q에 저장한다.
    for i in range(N):
        Q.append(i)
    # 화덕의 개수만큼 집어 넣고 남은 피자의 시작번호는 j와 같다.
    j = N
    # Q에 남은 피자가 1개이면 종료한다.
    while len(Q) > 1:
        a = Q.pop(0)
        cheeze[a] = cheeze[a] // 2
        if cheeze[a]:
            Q.append(a)
        else:
            if j <= M-1:
                Q.append(j)
                j += 1
    # 0부터 시작했으므로, 1을 더해준다.
    print("#{} {}".format(tc, Q[0]+1))





