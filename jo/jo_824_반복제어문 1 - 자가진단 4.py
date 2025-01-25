total = 0
cnt = 0
while True:
    num = int(input())
    total += num
    cnt += 1
    if num >= 100:
        break
print(total)
print(round(total/cnt, 1))