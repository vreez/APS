T = int(input())
for t in range(1, T+1):
    s1 = input()
    s2 = input()

    cnt = 0
    total = []
    for i in s1:
        cnt = 0
        for j in s2:
            if i == j:
                cnt += 1
        total.append(cnt)

    max_num = total[0]
    for x in total:
        if x >= max_num:
            max_num = x
    print("#{} {}".format(t, max_num))


