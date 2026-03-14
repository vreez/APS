arr = []
for i in range(7):
    num = int(input())
    if i == 0:
        arr.append(num + 2)
    elif i == 1:
        arr.append(num - 2)
    elif i == 2:
        arr.append(num * 2)
    elif i == 3:
        arr.append(num / 2)
    elif i == 4:
        arr.append(num // 2)
    elif i == 5:
        arr.append(num % 2)
    else:
        arr.append(num ** 2)

print(*arr)