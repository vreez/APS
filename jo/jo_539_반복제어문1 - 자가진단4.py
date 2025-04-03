N = list(map(int, input().split()))
total = 0
cnt = 0
for i in range(len(N)):
    if N[i] >= 100:
        total += N[i]
        cnt += 1
        break
    else:
        total += N[i]
        cnt += 1
print(total)
print(round(total/cnt, 1))
