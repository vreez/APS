cnt = 0
while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num % 3 != 0 and num % 5 != 0:
            cnt += 1
print(cnt)