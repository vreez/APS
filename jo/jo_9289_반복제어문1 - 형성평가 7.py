total = 0
cnt = 0
while True:
    num = int(input())
    if num > 5 or num < 1:
        break
    else:
        if num % 2 == 0:
            cnt += 1
            total += num
print(int(total/cnt))