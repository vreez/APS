N = list(map(int, input().split()))
total = 0
cnt = 0
for i in range(len(N)):
    if N[i] == 0:
        break
    else:
        if N[i] % 2 != 0:
            total += N[i]
            cnt += 1
print("홀수의 합 = {}".format(total))
print("홀수의 평균 = {}".format(total // cnt))