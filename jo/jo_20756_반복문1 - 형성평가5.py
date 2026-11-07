num = int(input())
total = 1
N = 1
while True:
    total *= N
    if total >= num:
        print(total)
        break
    N += 1