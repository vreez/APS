N = int(input())
cnt = 0
for i in range(N):
    s, c, a, r = map(int, input().split())
    if s >= 1000:
        cnt += 1
    else:
        if c >= 1600:
            cnt += 1
        else:
            if a >= 1500:
                cnt += 1
            else:
                if r <= 30 and r != -1:
                    cnt += 1
print(cnt)