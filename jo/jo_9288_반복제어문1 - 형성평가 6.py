cnt = 0
total = 0
while True:
    num = int(input())
    if num == 0:
        break
    else:
        cnt += 1
        total += num
print("cnt = {}".format(cnt))
print("sum = {}".format(total))