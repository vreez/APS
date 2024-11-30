num = 1
total = 0
while True:
    if num > 10:
        break
    else:
        total += num
        num += 1
print("1부터 10까지의 합 = {}".format(total))
print("while문이 끝난 후의 num의 값 = {}".format(num))