total = 0
cnt = 0
while True:
    num = int(input())
    if num < 0 or num > 100:
        break
    else:
        total += num
        cnt += 1
print("sum : {}".format(total))
print("avg : {:.1f}".format(total / cnt))
