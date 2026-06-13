N = int(input())
first = 0
second = 0
for i in range(N):
    num = int(input())
    if num % 2 == 0:
        second += 1
    else:
        first += num
print(first, second)