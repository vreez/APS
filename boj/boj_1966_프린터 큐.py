import sys; sys.stdin = open("1966.txt", "r")

tc = int(input())
for _ in range(tc):
    N, M = list(map(int, input().split()))
    imp = list(map(int, input().split()))

    queue = [[0, 0] for _ in range(N)]

    for i in range(N):
        queue[i][0] = imp[i]
        queue[i][1] = i

    answer = []
    while queue:
        maxDoc = max(queue)[0]
        if queue[0][0] == maxDoc:
            answer.append(queue[0][1])
            queue.pop(0)
        else:
            queue.append(queue[0])
            queue.pop(0)

    print(answer.index(M) + 1)


