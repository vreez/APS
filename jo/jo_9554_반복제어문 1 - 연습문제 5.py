total = 0
cnt = 0
while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num % 2 != 0:
            total += num
            cnt += 1

print("홀수의 합 = {}".format(total))
print("홀수의 평균 = {}".format(total // cnt))