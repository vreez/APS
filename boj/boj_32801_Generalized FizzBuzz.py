n, a, b = map(int, input().split())

fi, bu, fibu = 0, 0, 0
for i in range(1, n+1):
    if i % a == 0:
        if i % b == 0:
            fibu += 1
        else:
            fi += 1
    elif i % b == 0:
        bu += 1
print(fi, bu, fibu)
