N = list(map(int, input().split()))
total = 0
cnt = 0
for i in range(len(N)):
    if N[i] == 0:
        break
    else:
        total += N[i]
        cnt += 1
print("입력된 자료의 개수 = {}".format(cnt))
print("입력된 자료의 합계 = {}".format(total))
print("입력된 자료의 평균 = {}".format(round(total/cnt, 2)))