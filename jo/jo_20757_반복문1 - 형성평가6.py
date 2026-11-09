check = 0
while True:
    num = int(input())
    if num == 0:
        break
    else:
        if num % 2 == 0:
            check += 1
print(check)
