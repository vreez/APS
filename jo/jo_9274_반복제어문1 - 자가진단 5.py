N = int(input())

i = 0
ans = 0
while True:
    if i >= N:
        break
    else:
        i += 1
        ans += i
print(ans)