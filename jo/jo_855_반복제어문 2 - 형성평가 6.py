a, b = map(int, input().split())
if a >= b:
    small = b
    big = a
else:
    small = a
    big = b
total = 0
cnt = 0
for i in range(small, big + 1):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        cnt += 1
print("sum : {}".format(total))
print("avg : {}".format(round(total/cnt, 1)))
