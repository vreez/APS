a, b = map(int, input().split())
cnt = 0
for i in range(a, b+1):
    if i % 4 == 0 and i % 100 != 0:
        cnt += 1
    elif i % 400 == 0:
        cnt += 1
print(cnt)