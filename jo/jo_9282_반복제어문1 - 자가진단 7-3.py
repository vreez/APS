cnt = 0
total = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        if n < 1 or n > 100:
            continue
        else:
            cnt += 1
            total += n
print("count = {}".format(cnt))
print("total = {}".format(total))
print("avg = {}".format(total//cnt))
            