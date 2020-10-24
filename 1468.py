import sys; sys.stdin = open("1486.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    clerk = list(map(int, input().split()))

    count = 0
    total = []
    my_list = []
    def subset(k, N):
        if k == N:
            total.append(sum(my_list))
        else:
            my_list.append(clerk[k])
            subset(k+1, N)
            my_list.pop()
            subset(k+1, N)

    subset(0, N)
    new_total = sorted(total)
    for i in range(len(new_total)):
        if new_total[i] >= B:
            print("#{} {}".format(tc, new_total[i]-B))
            break