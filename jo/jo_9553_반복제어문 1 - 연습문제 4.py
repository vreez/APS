cnt = 0
total = 0
while True:
    num = int(input())
    if num == 0:
        break
    else:
        cnt += 1
        total += num
print("입력된 자료의 개수 = {}".format(cnt))
print("입력된 자료의 합계 = {}".format(total))
avg = total / cnt
print("입력된 자료의 평균 = {}".format(round(avg, 2)))