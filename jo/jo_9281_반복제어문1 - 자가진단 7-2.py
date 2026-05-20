ans = 0
while True:
    n = int(input())
    if n == 0:
        break
    elif n < 0:
        continue
    else:
        ans += n
print(ans)
